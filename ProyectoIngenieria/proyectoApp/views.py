from django.shortcuts import render, redirect, HttpResponseRedirect
from proyectoApp.form import LoginSupervisorForm, LoginControladorForm
from proyectoApp.models import Area, Empleado,Cuestionario, Pregunta, PreguntaRespondida, CuestionarioRespondido
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from proyectoApp.helpers import AreaEstructura, Empleado_Max
from django.http import JsonResponse
from proyectoApp.models import Pregunta_Filtro
from django.core.mail import send_mail

#Vistas del controlador

def salir(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def pregunta_Filtro (request):
    pregunta = Pregunta_Filtro.objects.get(pk=1)

    return render (request, 'Pregunta_Filtro.html',{'pregunta':pregunta})

@login_required(login_url='/')
def areas (request):
    areas = Area.objects.filter(estado = True)
    for i in areas:
        print(i.nombreArea,i.pk)
    return render(request, 'Areas.html', {'areas': areas})

@login_required(login_url='/')
def cuestionario (request,pk):
    cuestionario = Cuestionario.objects.get(area__pk=pk)
    preguntas = Pregunta.objects.filter(cuestionario__pk=cuestionario.pk)

    if request.method =="POST":
        area = Area.objects.get(pk=pk)
        user = request.user.username
        title = cuestionario.titulo
        user = User.objects.get(username = user)
        cuestionarioResp =CuestionarioRespondido(
            area= area,
            usuario = user,
            titulo = title
        )
        cuestionarioResp.save()


        for num in range(len(preguntas)):
            preg = preguntas[num]
            respuestaRes = request.POST.get(str(num+1))
            preguntaResp = PreguntaRespondida(
                pregunta = preg,
                respuesta = respuestaRes,
                CuestionarioRespondido = cuestionarioResp
            )
            preguntaResp.save()
            supervisores = list(Empleado.objects.filter(puesto__nombrePuesto ='Supervisor').values_list('email',flat = True))

        send_mail(
            'Se realizado un nuevo cuestionario',
    'El usuario: '+ str(user) + ' ha realizado un nuevo cuestionario en '+str(area),
    'emigdiosanchez22@gmail.com',
    supervisores,
    fail_silently=False,
            )


        return HttpResponseRedirect("/mensaje")


    return render(request, 'Cuestionario.html',{'Q':preguntas})



def mensaje (request):

    return render (request, 'mensaje.html')


def loginPrincipal (request):
    form = LoginSupervisorForm()
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        authUser = authenticate(request,username=username, password = password)
        if authUser:
            login(request,authUser)

            user = Empleado.objects.get(user=request.user)
            if user:
                if str(user.puesto) == "Supervisor":
                    return HttpResponseRedirect('/supervisor/')
                elif str(user.puesto) == "Controlador":
                    return HttpResponseRedirect('/preguntafiltro')
                elif str(user.puesto) == "RRHH":
                    return HttpResponseRedirect('/reportes')
    else:
        form = LoginSupervisorForm()

    return render (request, 'Login.html',{'form':form})

# Vista del Login de Controaldor LMV



#######################----------------Reportes --------------------------------###############################

@login_required(login_url='/')
def reportes (request):

    return render (request, 'Reportes.html')

@login_required(login_url='/')
def area_max_resp(request):
    lista_cantidad = []
    lista_area =[]
    areas = list(Area.objects.all().values_list('nombreArea', flat = True))
    for i in areas:
        cantidad = len (CuestionarioRespondido.objects.filter(area__nombreArea=i))
        if cantidad> 0:
            lista_cantidad.append(cantidad)
            lista_area.append(i)
    data={
        'labels': lista_area,
        'data':lista_cantidad
    }


    return render(request,'area_max.html',data)

@login_required(login_url='/')
def user_area_max(request):
    dicts = {}
    lista_user = []
    data = {}
    cont=0
    users = User.objects.all()
    areas = list(Area.objects.all().values_list('nombreArea', flat = True))
    for user in users:
        cont = 0
        for i in areas:
            cantidad = CuestionarioRespondido.objects.filter(area__nombreArea=i, usuario = user)
            print(cantidad)
            if cantidad.count() > 0:
                cont += cantidad.count()
        if cont>0:
            dicts[str(user)]= str(cont)
    data={
            'labels':list(dicts.keys()),
            'data': list(dicts.values()),
    }



    return render(request,'user_cuestionario_max.html',data)

@login_required(login_url='/')
def users_last_login(request):
    empleados = Empleado.objects.filter(puesto__nombrePuesto='Controlador')
    for empleado in empleados:
        print(empleado.user.username)

    return render(request,'user_last_login.html', {'empleados': empleados} )

@login_required(login_url='/')
def supervisor(request):
    empleados = Empleado.objects.filter(puesto__nombrePuesto='Controlador')
    areas = Area.objects.all()
    getArea = request.GET.get('area')
    getUsuario = request.GET.get('usuario')
    if getArea and getUsuario and request.method != 'POST':
        cuestionario = Cuestionario.objects.get(area__nombreArea =getArea)
        preguntas = Pregunta.objects.filter(cuestionario__pk = cuestionario.pk)

        return render( request, 'Preguntas_Supervisor.html',{'empleados':empleados,'areas':areas,'controlador':getUsuario, 'Q':preguntas,'getArea':getArea})

    if request.method == 'POST':
        controlador= request.POST.get('inputControlador','')
        getAreas= request.POST.get('inputArea','')

        areaCuestionario = Area.objects.get(nombreArea = getAreas)
        cuestionario_supervirsor = Cuestionario.objects.get(area__pk =areaCuestionario.pk)
        userCuestionario = User.objects.get(username = controlador)
        preguntas =Pregunta.objects.filter(cuestionario__pk =cuestionario_supervirsor.pk)
        cuestionarioResp =CuestionarioRespondido(
            es_supervisor = True,
            area= areaCuestionario,
            usuario = userCuestionario,
            titulo = cuestionario_supervirsor.titulo
        )
        cuestionarioResp.save()

        for num in range(len(preguntas)):
            preg = preguntas[num]
            respuestaRes = request.POST.get(str(num+1))
            preguntaResp = PreguntaRespondida(
                pregunta = preg,
                respuesta = respuestaRes,
                CuestionarioRespondido = cuestionarioResp
            )
            preguntaResp.save()
            supervisores = list(Empleado.objects.filter(puesto__nombrePuesto ='Supervisor').values_list('email',flat = True))

        send_mail(
            'Se realizado un nuevo cuestionario',
    'El usuario: '+ str(controlador) + ' ha realizado un nuevo cuestionario en '+str(getArea)+' por el supervisor',
    'emigdiosanchez22@gmail.com',
    supervisores,
    fail_silently=False,
            )
        return HttpResponseRedirect('/supervisor/')






    return render(request,'Preguntas_Supervisor.html',{'empleados':empleados,'areas':areas})

@login_required(login_url='/')
def user_filter(request):

    empleados = Empleado.objects.filter(puesto__nombrePuesto='Controlador')

    getUsuario = request.GET.get('usuario')
    if getUsuario:
        getUsuario=Empleado.objects.get(user__username=getUsuario)
        cuestionarios = CuestionarioRespondido.objects.filter(usuario__username=getUsuario.user.username)
        cuestionario = cuestionarios.order_by('fechaRealizacion')


        data = {'empleados':empleados,'cuestionarios':cuestionario}
        return render(request,'UserFilter.html',data)
    data = {'empleados':empleados}

    return render(request,'UserFilter.html',data)

@login_required(login_url='/')
def ver_preguntas(request,pk):
    titulo = CuestionarioRespondido.objects.get(pk=pk)
    preguntas = PreguntaRespondida.objects.filter(CuestionarioRespondido__pk =pk)
    if preguntas:

        return render(request,'preguntas_respondidas.html',{'preguntas':preguntas,'titulo':titulo})

    return HttpResponseRedirect('/filter-user/')
