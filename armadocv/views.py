from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render
import csv
from mailmerge import MailMerge

DATOS = 0


def armado_curriculum(request):

    return render(request, "index.html", {})


def envio_curriculum(request):

    name = request.POST["nombre"]
    apellido = request.POST["apellido"]
    fecha_de_nacimiento = request.POST["fecha-de-nacimiento"]
    lugar_de_nacimiento = request.POST["lugar-de-nacimiento"]
    edad = request.POST["edad"]
    dni = request.POST["dni"]
    cuil = request.POST["cuil"]
    estado_civil = request.POST.get("estado", " ")
    direccion = request.POST["direccion"]
    altura = request.POST["altura"]
    localidad = request.POST["localidad"]
    celular = request.POST["celular"]
    correo = request.POST["correo"]
    primario = request.POST.get("primario", " ")
    institucion_primario = request.POST["institucion-primario"]
    secundario = request.POST.get("secundario", " ")
    institucion_secundario = request.POST["institucion-secundario"]
    titulo_secundario = request.POST["titulo-secundario"]
    terciario = request.POST.get("terciario", " ")
    institucion_terciario = request.POST["institucion-terciario"]
    titulo_terciario = request.POST["titulo-terciario"]
    universitario = request.POST.get("universitario", " ")
    institucion_universitario = request.POST["institucion-universitario"]
    titulo_universitario = request.POST["titulo-universitario"]
    otros_conocimientos = request.POST["otros-conocimientos"]
    cursos = request.POST["cursos"]
    idiomas = request.POST.get("idiomas", " ")
    nombre_empresa_uno = request.POST["empresa-uno"]
    tareas_empresa_uno = request.POST.get("tareas-uno", " ")
    periodo_empresa_uno = request.POST["periodo-uno"]
    referencia_empresa_uno = request.POST["referencia-uno"]
    nombre_empresa_dos = request.POST["empresa-dos"]
    tareas_empresa_dos = request.POST.get("tareas-dos", " ")
    periodo_empresa_dos = request.POST["periodo-dos"]
    referencia_empresa_dos = request.POST["referencia-dos"]
    nombre_empresa_tres = request.POST["empresa-tres"]
    tareas_empresa_tres = request.POST.get("tareas-tres", " ")
    periodo_empresa_tres = request.POST["periodo-tres"]
    referencia_empresa_tres = request.POST["referencia-tres"]
    nombre_empresa_cuatro = request.POST["empresa-cuatro"]
    tareas_empresa_cuatro = request.POST.get("tareas-cuatro", " ")
    periodo_empresa_cuatro = request.POST["periodo-cuatro"]
    referencia_empresa_cuatro = request.POST["referencia-cuatro"]
    experiencias = request.POST.get("experiencias", " ")
    perfil = request.POST.get("perfil", " ")

    datos_cv = [{"nombre": name, "apellido": apellido,
                 "fecha_de_nacimiento": fecha_de_nacimiento, "lugar_de_nacimiento": lugar_de_nacimiento,
                 "edad": edad, "dni": dni, "cuil": cuil, "estado_civil": estado_civil, "direccion": direccion, "altura": altura,
                 "localidad": localidad,
                 "celular": celular, "correo": correo, "primario": primario,
                 "institucion_primario": institucion_primario, "secundario": secundario, 
                 "institucion_secundario": institucion_secundario, "titulo_secundario": titulo_secundario,
                 "terciario": terciario,
                 "institucion_terciario": institucion_terciario, "titulo_terciario": titulo_terciario,
                  "universitario": universitario,
                 "institucion_universitario": institucion_universitario, "titulo_universitario": titulo_universitario,
                 "otros_conocimientos": otros_conocimientos, "cursos": cursos, "idiomas": idiomas,
                 "nombre_empresa_uno": nombre_empresa_uno, "tareas_empresa_uno": tareas_empresa_uno,
                 "periodo_empresa_uno": periodo_empresa_uno, "referencia_empresa_uno": referencia_empresa_uno,
                 "nombre_empresa_dos": nombre_empresa_dos, "tareas_empresa_dos": tareas_empresa_dos,
                 "periodo_empresa_dos": periodo_empresa_dos, "referencia_empresa_dos": referencia_empresa_dos,
                 "nombre_empresa_tres": nombre_empresa_tres, "tareas_empresa_tres": tareas_empresa_tres,
                 "periodo_empresa_tres": periodo_empresa_tres, "referencia_empresa_tres": referencia_empresa_tres,
                 "nombre_empresa_cuatro": nombre_empresa_cuatro, "tareas_empresa_cuatro": tareas_empresa_cuatro,
                 "periodo_empresa_cuatro": periodo_empresa_cuatro, "referencia_empresa_cuatro": referencia_empresa_cuatro,
                 "experiencias": experiencias, "perfil": perfil
                }]

    # # field names
    # columnas = ['nombre']

    # # name of csv file
    # nombre_archivo = "datos_curriculum.csv"

    # # writing to csv file
    # with open(nombre_archivo, 'w') as csvfile:
    #     # creating a csv dict writer object
    #     writer = csv.DictWriter(csvfile, fieldnames=columnas)

    #     # writing headers (field names)
    #     writer.writeheader()

    #     # writing data rows
    #     writer.writerows(datos_cv)

    generar_docx(datos_cv)

    return render(request, "envio.html", context=datos_cv[DATOS])


def generar_docx(datos_cv):
    archivo = "Templates/plantilla-cv.docx"
    document = MailMerge(archivo)
    datos = datos_cv[DATOS]

    document.merge(nombre_apellido=datos["nombre"] + ' ' + datos["apellido"],
                   fecha_de_nacimiento=datos["fecha_de_nacimiento"],
                   lugar_de_nacimiento=datos["lugar_de_nacimiento"],
                   edad=datos["edad"],
                   dni=datos["dni"],
                   cuil=datos["cuil"],
                   estado_civil=datos["estado_civil"],
                   direccion=datos["direccion"] + ' ' + datos["altura"],
                   localidad=datos["localidad"],
                   celular=datos["celular"],
                   correo=datos["correo"], primario=datos["primario"],
                   institucion_primario=datos["institucion_primario"],
                   secundario=datos["secundario"],
                   institucion_secundario=datos["institucion_secundario"],
                   titulo_secundario=datos["titulo_secundario"],
                   terciario=datos["terciario"],
                   institucion_terciario=datos["institucion_terciario"],
                   titulo_terciario=datos["titulo_terciario"],
                   universitario=datos["universitario"],
                   institucion_universitario=datos["institucion_universitario"],
                   titulo_universitario=datos["titulo_universitario"],
                   otros_conocimientos=datos["otros_conocimientos"],
                   cursos=datos["cursos"],
                   idiomas=datos["idiomas"],
                   nombre_empresa_uno = datos["nombre_empresa_uno"], 
                   tareas_empresa_uno = datos["tareas_empresa_uno"],
                   periodo_empresa_uno = datos["periodo_empresa_uno"], 
                   referencia_empresa_uno = datos["referencia_empresa_uno"],
                   nombre_empresa_dos = datos["nombre_empresa_dos"],
                   tareas_empresa_dos = datos["tareas_empresa_dos"],
                   periodo_empresa_dos = datos["periodo_empresa_dos"], 
                   referencia_empresa_dos = datos["referencia_empresa_dos"],
                   nombre_empresa_tres = datos["nombre_empresa_tres"], 
                   tareas_empresa_tres = datos["tareas_empresa_tres"],
                   periodo_empresa_tres  = datos["periodo_empresa_tres"], 
                   referencia_empresa_tres = datos["referencia_empresa_tres"],
                   nombre_empresa_cuatro = datos["nombre_empresa_cuatro"], 
                   tareas_empresa_cuatro = datos["tareas_empresa_cuatro"],
                   periodo_empresa_cuatro = datos["periodo_empresa_cuatro"], 
                   referencia_empresa_cuatro = datos["referencia_empresa_cuatro"],
                   experiencias = datos["experiencias"], perfil = datos["perfil"]
                   )

    document.write('curriculums/' +
                   datos["nombre"] + ' ' + datos["apellido"] + '.docx')
