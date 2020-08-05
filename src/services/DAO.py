from src import db


class DAO:
    @staticmethod
    def get_by_id(class_name, object_id):
        return class_name.query.get_or_404(object_id)

    @staticmethod
    def get_all(class_name):
        return class_name.query.all()

    @staticmethod
    def delete_by_id(class_name, object_id):
        class_name.query.filter(class_name.id == object_id).delete()
        db.session.commit()

    @staticmethod
    def create(class_name, attrs_dict):
        new = class_name()
        for key, val in attrs_dict.items():
            setattr(new, key, val)

        db.session.add(new)
        db.session.commit()

    @staticmethod
    def update(class_name, object_id, attrs_dict):
        update_object = class_name.query.get_or_404(object_id)
        for key, val in attrs_dict.items():
            if key is not 'submit' and key is not 'csrf_token':
                setattr(update_object, key, val)
        db.session.commit()
