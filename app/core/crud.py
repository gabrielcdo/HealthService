from sqlalchemy.orm import Session
from . import models, schemas

def agendar_consulta(db: Session, consulta: schemas.ConsultaCreate):
    db_consulta = models.Consulta(
        idpaciente=consulta.id_paciente,
        idmedico=consulta.id_medico,
        data_consulta=consulta.data_consulta,
        horario_consulta=consulta.horario_consulta,
    )
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta

def cancelar_consulta(db: Session, consulta_id: int, status: str = "Cancelada"):
    db_consulta = db.query(models.Consulta).filter(models.Consulta.id_consulta == consulta_id).first()
    if db_consulta:
        db_consulta.status = status  # Atualiza o status para "Cancelada"
        db.commit()
        db.refresh(db_consulta)
        return db_consulta
    return None
