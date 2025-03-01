from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core import models
from app.schemas import schemas
from app.services.database import get_db


router = APIRouter()


# Atualizar paciente
@router.put("/pacientes/{idpaciente}", response_model=schemas.Paciente)
def atualizar_paciente(idpaciente: int, paciente: schemas.Paciente, db: Session = Depends(get_db)):
    paciente_atualizado = db.query(models.Paciente).filter(models.Paciente.idpaciente == idpaciente).first()
    if not paciente_atualizado:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    for key, value in paciente.dict().items():
        setattr(paciente_atualizado, key, value)
    
    db.commit()
    db.refresh(paciente_atualizado)
    return paciente_atualizado

# Deletar paciente
@router.delete("/pacientes/{idpaciente}", response_model=schemas.Paciente)
def deletar_paciente(idpaciente: int, db: Session = Depends(get_db)):
    paciente = db.query(models.Paciente).filter(models.Paciente.idpaciente == idpaciente).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    db.delete(paciente)
    db.commit()
    return paciente


# Criar paciente
@router.post("/pacientes/", response_model=schemas.Paciente)
def criar_paciente(paciente: schemas.Paciente, db: Session = Depends(get_db)):
    novo_paciente = models.Paciente(**paciente.dict())
    db.add(novo_paciente)
    db.commit()
    db.refresh(novo_paciente)
    return novo_paciente

# Listar pacientes
@router.get("/pacientes/", response_model=list[schemas.Paciente])
def listar_pacientes(db: Session = Depends(get_db)):
    return db.query(models.Paciente).all()


# Atualizar médico
@router.put("/medicos/{idmedico}", response_model=schemas.Medico)
def atualizar_medico(idmedico: int, medico: schemas.Medico, db: Session = Depends(get_db)):
    medico_atualizado = db.query(models.Medico).filter(models.Medico.idmedico == idmedico).first()
    if not medico_atualizado:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    
    for key, value in medico.dict().items():
        setattr(medico_atualizado, key, value)
    
    db.commit()
    db.refresh(medico_atualizado)
    return medico_atualizado

# Deletar médico
@router.delete("/medicos/{idmedico}", response_model=schemas.Medico)
def deletar_medico(idmedico: int, db: Session = Depends(get_db)):
    medico = db.query(models.Medico).filter(models.Medico.idmedico == idmedico).first()
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    
    db.delete(medico)
    db.commit()
    return medico

# Criar médico
@router.post("/medicos/", response_model=schemas.Medico)
def criar_medico(medico: schemas.Medico, db: Session = Depends(get_db)):
    novo_medico = models.Medico(**medico.dict())
    db.add(novo_medico)
    db.commit()
    db.refresh(novo_medico)
    return novo_medico


# Listar médicos
@router.get("/medicos/", response_model=list[schemas.Medico])
def listar_medicos(db: Session = Depends(get_db)):
    return db.query(models.Medico).all()


# Criar consulta
@router.post("/consultas/", response_model=schemas.Consulta)
def criar_consulta(consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    nova_consulta = models.Consulta(**consulta.dict())
    db.add(nova_consulta)
    db.commit()
    db.refresh(nova_consulta)
    return nova_consulta

# Listar consultas
@router.get("/consultas/", response_model=list[schemas.Consulta])
def listar_consultas(db: Session = Depends(get_db)):
    return db.query(models.Consulta).all()

# Atualizar especialidade
@router.put("/especialidades/{idespecialidade}", response_model=schemas.Especialidades)
def atualizar_especialidade(idespecialidade: int, especialidade: schemas.Especialidades, db: Session = Depends(get_db)):
    especialidade_atualizada = db.query(models.Especialidade).filter(models.Especialidade.idespecialidade == idespecialidade).first()
    if not especialidade_atualizada:
        raise HTTPException(status_code=404, detail="Especialidade não encontrada")
    
    for key, value in especialidade.dict().items():
        setattr(especialidade_atualizada, key, value)
    
    db.commit()
    db.refresh(especialidade_atualizada)
    return especialidade_atualizada

# Deletar especialidade
@router.delete("/especialidades/{idespecialidade}", response_model=schemas.Especialidades)
def deletar_especialidade(idespecialidade: int, db: Session = Depends(get_db)):
    especialidade = db.query(models.Especialidade).filter(models.Especialidade.idespecialidade == idespecialidade).first()
    if not especialidade:
        raise HTTPException(status_code=404, detail="Especialidade não encontrada")
    
    db.delete(especialidade)
    db.commit()
    return especialidade

# Listar consultas
@router.get("/especialidades/", response_model=list[schemas.Especialidades])
def listar_consultas(db: Session = Depends(get_db)):
    return db.query(models.Especialidade).all()


@router.post("/especialidades/", response_model=schemas.Especialidades)
def criar_consulta(especialidade: schemas.Especialidades, db: Session = Depends(get_db)):
    nova_especialidade = models.Especialidade(**especialidade.dict())
    db.add(nova_especialidade)
    db.commit()
    db.refresh(nova_especialidade)
    return nova_especialidade


# Atualizar consulta
@router.put("/consultas/{idconsulta}", response_model=schemas.Consulta)
def atualizar_consulta(idconsulta: int, consulta: schemas.ConsultaUpdate, db: Session = Depends(get_db)):
    consulta_atualizada = db.query(models.Consulta).filter(models.Consulta.idconsulta == idconsulta).first()
    if not consulta_atualizada:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    
    for key, value in consulta.dict().items():
        setattr(consulta_atualizada, key, value)
    
    db.commit()
    db.refresh(consulta_atualizada)
    return consulta_atualizada

# Deletar consulta
@router.delete("/consultas/{idconsulta}", response_model=schemas.Consulta)
def deletar_consulta(idconsulta: int, db: Session = Depends(get_db)):
    consulta = db.query(models.Consulta).filter(models.Consulta.idconsulta == idconsulta).first()
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    
    db.delete(consulta)
    db.commit()
    return consulta


from datetime import datetime

@router.post("/consultas/", response_model=schemas.Consulta)
def criar_consulta(consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    # Verificar se o paciente existe
    paciente = db.query(models.Paciente).filter(models.Paciente.idpaciente == consulta.idpaciente).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    # Verificar se o médico existe
    medico = db.query(models.Medico).filter(models.Medico.idmedico == consulta.idmedico).first()
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")

    # Verificar se a data e hora da consulta são válidas
    try:
        # Verificar se a data da consulta é no futuro
        if consulta.dataconsulta < datetime.today().date():
            raise HTTPException(status_code=400, detail="A data da consulta não pode ser no passado.")
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de data inválido.")
    
    nova_consulta = models.Consulta(**consulta.dict())
    db.add(nova_consulta)
    db.commit()
    db.refresh(nova_consulta)
    return nova_consulta


@router.get("/consultas/paciente/{idpaciente}", response_model=list[schemas.Consulta])
def listar_consultas_por_paciente(idpaciente: int, db: Session = Depends(get_db)):
    paciente = db.query(models.Paciente).filter(models.Paciente.idpaciente == idpaciente).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")
    
    consultas = db.query(models.Consulta).filter(models.Consulta.idpaciente == idpaciente).all()
    if not consultas:
        raise HTTPException(status_code=404, detail="Nenhuma consulta encontrada para esse paciente.")
    
    return consultas


@router.get("/consultas/medico/{idmedico}", response_model=list[schemas.Consulta])
def listar_consultas_por_medico(idmedico: int, db: Session = Depends(get_db)):
    medico = db.query(models.Medico).filter(models.Medico.idmedico == idmedico).first()
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado.")
    
    consultas = db.query(models.Consulta).filter(models.Consulta.idmedico == idmedico).all()
    if not consultas:
        raise HTTPException(status_code=404, detail="Nenhuma consulta encontrada para esse médico.")
    
    return consultas
