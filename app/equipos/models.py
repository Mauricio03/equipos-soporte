from app import db
from datetime import *
import datetime


#Tabla de Equipos
class InfoSoporte(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255))
    marca = db.Column(db.String(255))
    modelo = db.Column(db.String(255))
    sn = db.Column(db.String(255))
    tinco = db.Column(db.String(255))
    plataforma = db.Column(db.String(255))
    datacenter = db.Column(db.String(255))
    sala = db.Column(db.String(255))
    rack = db.Column(db.String(255))
    proveedor = db.Column(db.String(255))
    soporte = db.Column(db.Date)

    def __repr__(self):
        return f'<InfoSoporte {self.modelo}>'

    def save(self):
        if not self.id:
            db.session.add(self)
            db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, tipo, marca, modelo, sn, tinco, plataforma, datacenter, sala, rack, proveedor, soporte):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.sn = sn
        self.tinco = tinco
        self.plataforma = plataforma
        self.datacenter = datacenter
        self.sala = sala
        self.rack = rack
        self.proveedor = proveedor
        self.soporte = soporte
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return InfoSoporte.query.get(id)

    @staticmethod
    def get_by_sn(sn):
        return InfoSoporte.query.filter_by(sn=sn).first()


    @staticmethod
    def get_by_sn2(sn, page=1, per_page=30):
        return InfoSoporte.query.filter_by(sn=sn).paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_by_dc(dc, page=1, per_page=30):
        return InfoSoporte.query.filter_by(datacenter=dc).paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_by_soporte_vencido(dc, page=1, per_page=30):
        if dc is None:
            return InfoSoporte.query.filter(InfoSoporte.soporte < date.today()).paginate(page=page, per_page=per_page, error_out=False)
        else:
            return InfoSoporte.query.filter(InfoSoporte.datacenter==dc, InfoSoporte.soporte < date.today()).paginate(page=page, per_page=per_page, error_out=False)


    @staticmethod
    def get_by_soporte_activo(dc, page=1, per_page=30):
        if dc is None:
            return InfoSoporte.query.filter(InfoSoporte.soporte >= date.today()).paginate(page=page, per_page=per_page, error_out=False)
        else:
            return InfoSoporte.query.filter(InfoSoporte.datacenter==dc, InfoSoporte.soporte >= date.today()).paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_by_prox_vencimiento(dc, dias, page=1, per_page=30):
        if dc is None:
            return InfoSoporte.query.filter(InfoSoporte.soporte >= date.today(), InfoSoporte.soporte <= date.today() + datetime.timedelta(days=dias)).paginate(page=page, per_page=per_page, error_out=False)
        else:
            return InfoSoporte.query.filter(InfoSoporte.soporte >= date.today(), InfoSoporte.soporte <= date.today() + datetime.timedelta(days=dias), InfoSoporte.datacenter==dc).paginate(page=page, per_page=per_page, error_out=False)


    @staticmethod
    def get_by_vencimiento(dias):
        if dias == 0:
            return InfoSoporte.query.filter(InfoSoporte.soporte < date.today()).all()
        elif dias == 30:
            return InfoSoporte.query.filter(InfoSoporte.soporte >= date.today(), InfoSoporte.soporte <= date.today() + datetime.timedelta(days=dias)).all()
        elif dias == 90:
            return InfoSoporte.query.filter(InfoSoporte.soporte > date.today() + datetime.timedelta(days=30), InfoSoporte.soporte <= date.today() + datetime.timedelta(days=dias)).all()
        elif dias == 180:
            return InfoSoporte.query.filter(InfoSoporte.soporte > date.today() + datetime.timedelta(days=90), InfoSoporte.soporte <= date.today() + datetime.timedelta(days=dias)).all()
        else:
            return InfoSoporte.query.all()


    @staticmethod
    def get_all():
        return InfoSoporte.query.all()

    @staticmethod
    def all_paginated(page=1, per_page=30):
        return InfoSoporte.query.order_by(InfoSoporte.id.asc()).paginate(page=page, per_page=per_page, error_out=False)
