from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from datetime import *

class EquipoForm(FlaskForm):
    tipo = SelectField('Tipo', choices=[('Servidor', 'Servidor'),('Switch', 'Switch'),('Firewall','Firewall'),('Balanceador','Balanceador'),('Storage','Storage'),('Router','Router')])
    marca = SelectField('Marca', choices=[('Cisco','Cisco'),('Dell','Dell'),('IBM','IBM'),('EMC','EMC'),('Huawei','Huawei'),('HP','HP'),('Alcatel','Alcatel')])
    modelo = StringField('Modelo')
    sn = StringField('S/N')
    tinco = StringField('Tinco')
    plataforma = SelectField('Plataforma', choices=[('Cloud Lezama','Cloud Lezama'),('Cloud Pando','Cloud Pando'),('Vera Pando','Vera Pando'),('Vera TV','Vera TV'),('Correo Vera','Correo Vera')])
    datacenter = SelectField('Datacenter', choices=[('DC Lezama','DC Lezama'),('DC Pando','DC Pando'),('Mercedes','Mercedes')], default='DC Lezama')
    salaLezama = SelectField('Sala', choices=[('Sala de Datos Piso 2', 'Sala de Datos Piso 2')])
    salaPando = SelectField('Sala', choices=[('Sala de Datos 1', 'Sala de Datos 1')])
    salaMercedes = SelectField('Sala', choices=[('ExIBM', 'ExIBM'),('NDC', 'NDC')])
    rackLezamaPiso2 = SelectField('Rack', choices=[('AI07', 'AI07'),('AI09', 'AI09'),('AI18', 'AI18'),('AI19', 'AI19'),('AI20', 'AI20'),('AM05', 'AM05'),('AM06', 'AM06'),('AM07', 'AM07'),('AM08', 'AM08'),('AM09', 'AM09'),('AM10', 'AM10'),('AM17', 'AM17')])
    rackPandoSala1 = SelectField('Rack', choices=[('1C25', '1C25'),('1C28B', '1C28B'),('1D10', '1D10'),('1D11', '1D11'),('1D23', '1D23')])
    rackMercedesExIBM = SelectField('Rack', choices=[('1', '1'),('2', '2'),('3', '3')])
    rackMercedesNDC = SelectField('Rack', choices=[('6G', '6G'),('12A', '12A'),('12C', '12C')])
    proveedor = SelectField('Proveedor', choices=[('Datacenter','Datacenter'),('Logicalis','Logicalis'),('ACCSA','ACCSA'),('INCO','INCO'),('Conatel','Conatel'),('Nokia','Nokia'),('Isbel','Isbel')])
    soporte = DateField('Vencimiento_Soporte', default=date.today(), format='%d-%m-%Y')
    post_equipo = SubmitField('Agregar')
    editar_equipo = SubmitField('Actualizar')
