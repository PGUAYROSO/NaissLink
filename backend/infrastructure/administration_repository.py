from app.extensions import db

from domain.utilisateur import Utilisateur
from domain.dossier import DossierDocumentaire
from domain.document import Document
from domain.transmission import Transmission
from domain.type_document import TypeDocument
from domain.audit_log import AuditLog


class AdministrationRepository:

    @staticmethod
    def compter_utilisateurs():
        return db.session.query(Utilisateur).count()

    @staticmethod
    def compter_dossiers():
        return db.session.query(DossierDocumentaire).count()

    @staticmethod
    def compter_documents():
        return db.session.query(Document).count()

    @staticmethod
    def compter_transmissions():
        return db.session.query(Transmission).count()

    @staticmethod
    def compter_types_documents():
        return db.session.query(TypeDocument).count()

    @staticmethod
    def compter_audit_logs():
        return db.session.query(AuditLog).count()

    @staticmethod
    def derniers_audits(limite=10):
        return (
            AuditLog.query
            .order_by(AuditLog.date_action.desc())
            .limit(limite)
            .all()
        )