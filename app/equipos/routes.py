from email.mime.application import MIMEApplication
from flask import render_template, request, redirect, url_for, current_app, flash
from flask_login import login_required, current_user
from werkzeug.urls import url_parse
from werkzeug.exceptions import NotFound
import logging
from flask_mail import Message
from datetime import *
import pdfkit

from .models import InfoSoporte
from . import equipos_bp
from .forms import EquipoForm
from app.mails.mail import send_email

logger = logging.getLogger(__name__)


#ENVIAR MAIL CON INFORME DE VENCIMIENTOS
@equipos_bp.route('/send_informe/')
@login_required
def send_informe():
    logger.info('Generar informe de vencimientos')
    equipos_vencidos = InfoSoporte.get_by_vencimiento(0)
    equipos_vencimiento_1 = InfoSoporte.get_by_vencimiento(30)
    equipos_vencimiento_3 = InfoSoporte.get_by_vencimiento(90)
    equipos_vencimiento_6 = InfoSoporte.get_by_vencimiento(180)
    html = render_template("informe.html", equipos_vencidos=equipos_vencidos, equipos_vencimiento_1=equipos_vencimiento_1, equipos_vencimiento_3=equipos_vencimiento_3, equipos_vencimiento_6=equipos_vencimiento_6, today=date.today())
    #pdf = pdfkit.from_string(html, False)
    #pdfkit.from_string(html, 'informe.pdf')
    #pdf = MIMEApplication(open("informe.pdf", 'rb').read())
    #print(pdf)
    #print(type(pdf))
    #pdf.add_header('Content-Disposition', 'attachment', filename= "informe.pdf")
    #pdf.add_header('Content-Type','application/pdf')
    logger.info('Mandar informe de vencimientos')
    send_email(subject='Informe vencimiento soporte Platafomas de Servicio',
               sender=current_app.config['DONT_REPLY_FROM_EMAIL'],
               recipients=["msosachocho@antel.com.uy"],
               text_body='',
               html_body=html)
               #,adjunto=pdf)
    flash('El informe se ha enviado a msosachocho@antel.com.uy')
    return redirect(url_for('equipos.index'))


#INDEX
@equipos_bp.route('/', defaults={'dc': None})
@equipos_bp.route('/<string:dc>/')
@login_required
def index(dc):
    page = int(request.args.get('page', 1))
    por_page = int(request.args.get('por_page', 20))
    if dc:
        if dc=='lezama':
            logger.info('Mostrando los equipos de DC Lezama')
            equipos = InfoSoporte.get_by_dc('DC Lezama', page, por_page)
        elif dc=='pando':
            logger.info('Mostrando los equipos de DC Pando')
            equipos = InfoSoporte.get_by_dc('DC Pando', page, por_page)
        elif dc=='mercedes':
            logger.info('Mostrando los equipos de Mercedes')
            equipos = InfoSoporte.get_by_dc('Mercedes', page, por_page)
        else:
            raise NotFound(dc)
    else:
        logger.info('Mostrando todos los equipos')
        equipos = InfoSoporte.all_paginated(page, por_page)
    return render_template("index.html", equipos=equipos, dc=dc, por_page=por_page, today=date.today())


#LISTAR EQUIPOS VENCIDOS
@equipos_bp.route('/vencidos/', defaults={'dc':None})
@equipos_bp.route('/vencidos/<string:dc>/')
@login_required
def vencidos(dc):
    page = int(request.args.get('page', 1))
    por_page = int(request.args.get('por_page', 20))
    if dc is None:
        logger.info('Mostrando los equipos vencidos')
        equipos = InfoSoporte.get_by_soporte_vencido(dc, page, por_page)
    else:
        if dc=='lezama':
            logger.info('Mostrando los equipos vencidos de DC Lezama')
            equipos = InfoSoporte.get_by_soporte_vencido('DC Lezama', page, por_page)
        elif dc=='pando':
            logger.info('Mostrando los equipos vencidos de DC Pando')
            equipos = InfoSoporte.get_by_soporte_vencido('DC Pando', page, por_page)
        elif dc=='mercedes':
            logger.info('Mostrando los equipos vencidos de Mercedes')
            equipos = InfoSoporte.get_by_soporte_vencido('Mercedes', page, por_page)
        else:
            raise NotFound(dc)
    return render_template("index.html", equipos=equipos, dc=dc, por_page=por_page, today=date.today())


#LISTAR EQUIPOS ACTIVOS
@equipos_bp.route('/activos/', defaults={'dc':None})
@equipos_bp.route('/activos/<string:dc>/')
@login_required
def activos(dc):
    page = int(request.args.get('page', 1))
    por_page = int(request.args.get('por_page', 20))
    if dc is None:
            logger.info('Mostrando los equipos activos')
            equipos = InfoSoporte.get_by_soporte_activo(dc, page, por_page)
    else:
        if dc=='lezama':
            logger.info('Mostrando los equipos activos de DC Lezama')
            equipos = InfoSoporte.get_by_soporte_activo('DC Lezama', page, por_page)
        elif dc=='pando':
            logger.info('Mostrando los equipos activos de DC Pando')
            equipos = InfoSoporte.get_by_soporte_activo('DC Pando', page, por_page)
        elif dc=='mercedes':
            logger.info('Mostrando los equipos activos de Mercedes')
            equipos = InfoSoporte.get_by_soporte_activo('Mercedes', page, por_page)
        else:
            raise NotFound(dc)
    return render_template("index.html", equipos=equipos, dc=dc, por_page=por_page, today=date.today())


#PROXIMOS VENCIMIENTOS
@equipos_bp.route('/prox_vencimientos/<int:dias>/', defaults={'dc':None})
@equipos_bp.route('/prox_vencimientos/<int:dias>/<string:dc>/')
@login_required
def prox_vencimientos(dias, dc):
    page = int(request.args.get('page', 1))
    por_page = int(request.args.get('por_page', 20))
    if dc is None:
        logger.info(f'Mostrando todos los equipos que vencen en menos de {dias} dias')
        equipos = InfoSoporte.get_by_prox_vencimiento(dc, dias, page, por_page)
    else:
        if dc=='lezama':
            logger.info(f'Mostrando los equipos que vencen en menos de {dias} dias de DC Lezama')
            equipos = InfoSoporte.get_by_prox_vencimiento('DC Lezama', dias, page, por_page)
        elif dc=='pando':
            logger.info(f'Mostrando todos los equipos que vencen en menos de {dias} dias de DC Pando')
            equipos = InfoSoporte.get_by_prox_vencimiento('DC Pando', dias, page, por_page)
        elif dc=='mercedes':
            logger.info(f'Mostrando todos los equipos que vencen en menos de {dias} dias de Mercedes')
            equipos = InfoSoporte.get_by_prox_vencimiento('Mercedes', dias, page, por_page)
        else:
            raise NotFound(dc)
    return render_template("index.html", equipos=equipos, dc=dc, por_page=por_page, today=date.today())


#BUSCADOR POR S/N
@equipos_bp.route('/buscador/', methods = ['POST','GET'])
@login_required
def buscador():
    page = int(request.args.get('page', 1))
    por_page = int(request.args.get('por_page', 20))
    sn = request.form['buscador']
    logger.info(f'Buscar el equipo con S/N: {sn}')
    if sn == '':
        return redirect(url_for('equipos.index'))
    else:
        equipo = InfoSoporte.get_by_sn(sn)
        if equipo is None:
            logger.info(f'El equipo buscado con S/N:{sn} no existe')
            flash(f'El equipo con S/N: {sn} no se encuentra en el sistema')
            return redirect(url_for('equipos.index'))
        else:
            logger.info(f'El S/N:{sn} fue encontrado en el sistema')
            equipo = InfoSoporte.get_by_sn2(sn, page, por_page)
            return render_template('index.html', equipos=equipo, por_page=por_page, today=date.today())


#AGREGAR O EDITAR EQUIPO
@equipos_bp.route('/post_equipo/', methods = ['POST','GET'], defaults={'id': None})
@equipos_bp.route('/post_equipo/<int:id>/', methods = ['GET','POST'])
@login_required
def post_equipo(id):
    form = EquipoForm()
    error = None
    if request.method == 'GET':
        if id:
            #editar equipo
            logger.info(f'Editar equipo: {id}')
            equipo = InfoSoporte.get_by_id(id)
            if equipo is None:
                logger.info(f'El equipo a editar con id {id} no existe')
                raise NotFound(id)
            form = EquipoForm(obj=equipo)
            if equipo.datacenter == 'DC Lezama':
                form.salaLezama.data == equipo.sala
                form.rackLezamaPiso2.data = equipo.rack
            elif equipo.datacenter == 'DC Pando':
                form.salaPando.data == equipo.sala
                form.rackPandoSala1.data = equipo.rack
            else:
                form.salaMercedes.data = equipo.sala
                if equipo.sala == 'ExIBM':
                    form.rackMercedesExIBM.data = equipo.rack
                else:
                    form.rackMercedesNDC.data = equipo.rack
        return render_template('post_equipo.html', form=form, id=id, error=error)
    else:
        #agregar o actualizar equipo
        logger.info('Agregar o actualizar equipo')
        tipo = form.tipo.data
        marca = form.marca.data
        modelo = form.modelo.data
        sn = form.sn.data
        tinco = form.tinco.data
        plataforma = form.plataforma.data
        datacenter = form.datacenter.data
        if datacenter=='DC Lezama':
            sala = form.salaLezama.data
            rack = form.rackLezamaPiso2.data
        elif datacenter=='DC Pando':
            sala = form.salaPando.data
            rack = form.rackPandoSala1.data
        else:
            sala = form.salaMercedes.data
            if sala == 'ExIBM':
                rack = form.rackMercedesExIBM.data
            else:
                rack = form.rackMercedesNDC.data
        proveedor = form.proveedor.data
        soporte = form.soporte.data
        if id:
            #actualizar equipo
            logger.info(f'Actualizar equipo: {id}')
            equipo = InfoSoporte.get_by_id(id)
            if equipo.sn != sn:
                equipo2 = InfoSoporte.get_by_sn(sn)
                if equipo2 is not None and sn!="":
                    logger.info(f'El nuevo S/N:{sn} del equipo {id} ya existe')
                    error = f'El S/N: {sn} ya está siendo utilizado por otro equipo'
                    return render_template('post_equipo.html', id=id, form=form, error=error)
            equipo.update(tipo, marca, modelo, sn, tinco, plataforma, datacenter, sala, rack, proveedor, soporte)
            logger.info(f'El equipo {id} ha sido editado')
            flash('El equipo ha sido correctamente')
            return redirect(url_for('equipos.index'))    
        else:
            #agregar equipo
            logger.info('Agregar nuevo equipo')
            equipo = InfoSoporte.get_by_sn(sn)
            if equipo is not None and sn!="":
                logger.info(f'El S/N:{sn} ya existe')
                error = f'El S/N {sn}: ya está siendo utilizado por otro equipo'
            else:
                logger.info(f'El S/N:{sn} a agregar es valido')
                equipo = InfoSoporte(tipo=tipo, marca=marca, modelo=modelo, sn=sn, tinco=tinco, plataforma=plataforma, datacenter=datacenter, sala=sala, rack=rack, proveedor=proveedor, soporte=soporte)
                equipo.save()
                logger.info(f'El equipo con S/N:{sn} ha sido agregado correctamente')
                flash('Nuevo equipo agregado correctamente')
                return redirect(url_for('equipos.index'))
            return render_template('post_equipo.html', id=id, form=form, error=error)


#ELIMINAR EQUIPO
@equipos_bp.route('/eliminar_equipo/<int:id>/', methods = ['GET','POST'])
@login_required
def eliminar_equipo(id):
    logger.info(f'Elminar equipo {id}')
    equipo = InfoSoporte.get_by_id(id)
    if equipo is None:
        logger.info(f'El equipo a eliminar con id {id} no existe')
        raise NotFound(id)
    equipo.delete()
    logger.info(f'El equipo {id} a sido eliminado')
    flash('El equipo ha sido eliminado correctamente')
    return redirect(url_for('equipos.index'))
