from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.services.database import Base

class Paciente(Base):
    __tablename__ = 'paciente'

    idpaciente = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    sobrenome = Column(String)
    cpf = Column(String, unique=True)
    telefone = Column(String)
    datanasc = Column(Date)




class Medico(Base):
    __tablename__ = 'medico'

    idmedico = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    sobrenome = Column(String)
    crm = Column(String, unique=True)
    diasatend = Column(String)
    horasatend = Column(String)
    

class Especialidade(Base):
    __tablename__ = 'especialidade'

    idespecialidade = Column(Integer, primary_key=True, index=True)
    nomeespecialidade = Column(String, unique=True)
    descricao = Column(String)
    idmedico = Column(Integer, ForeignKey('medico.idmedico'))



class Consulta(Base):
    __tablename__ = 'consulta'

    idconsulta = Column(Integer, primary_key=True, index=True)
    idpaciente = Column(Integer, ForeignKey('paciente.idpaciente'))  # Corrected the ForeignKey reference
    idmedico = Column(Integer, ForeignKey('medico.idmedico'))  # Corrected the ForeignKey reference
    dataconsulta = Column(Date)
    horarioconsulta = Column(Time)
    status = Column(String, default="Agendada")  # Para o soft delete, pode mudar o status para "Cancelada"
    dataagendamento = Column(Date)

    paciente = relationship("Paciente", back_populates="consultas")
    medico = relationship("Medico", back_populates="consultas")

Paciente.consultas = relationship("Consulta", back_populates="paciente")
Medico.consultas = relationship("Consulta", back_populates="medico")
