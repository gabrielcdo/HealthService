from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time

# Base models (no id field, for creating objects)
class PacienteBase(BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    telefone: str
    datanasc: date

class EspecialidadesBase(BaseModel):
    idmedico: int
    nomeespecialidade: str
    descricao: str

class MedicoBase(BaseModel):
    nome: str
    sobrenome: str
    crm: str
    diasatend: str
    horasatend: str

class ConsultaBase(BaseModel):
    idpaciente: int  # Reference to Paciente by id
    idmedico: int    # Reference to Medico by id
    dataconsulta: date
    horarioconsulta: time
    

# Models for creation and updates (inherits from base models)
class ConsultaCreate(ConsultaBase):
    pass

class ConsultaUpdate(ConsultaBase):
    status: Optional[str] = "Agendada"  # Default status if not provided

# Models that include 'id' and are used for returning objects (after creation)
class Paciente(PacienteBase):
    idpaciente: int  # 'id' instead of 'idpaciente' for consistency
    class Config:
        orm_mode = True
        
class Especialidades(EspecialidadesBase):
    idespecialidade: int  # 'id' instead of 'idpaciente' for consistency
    class Config:
        orm_mode = True

class Medico(MedicoBase):
    idmedico: int  # 'id' instead of 'idmedico' for consistency
    class Config:
        orm_mode = True

class Consulta(ConsultaBase):
    idconsulta: int  # 'id' instead of 'idconsulta' for consistency
    status: str
    dataagendamento: date
    paciente: Paciente
    medico: Medico
    class Config:
        orm_mode = True
        

