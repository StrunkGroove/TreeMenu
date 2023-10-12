from django.core.exceptions import ValidationError
from django.db import models


class TreeMenuValidator:
    @staticmethod
    def validate_no_slash(value):
        if '/' in value:
            raise ValidationError("Символ / недопустим в поле.")
    
class TreeMenu(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        validators=[TreeMenuValidator.validate_no_slash]
    )
    path = models.CharField(max_length=255, blank=True)
    table_name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
        
    @classmethod
    def get_ancestors(cls, name, table):
        name_model = cls._meta.db_table
        query = f"""
            SELECT id, name, path
            FROM {name_model} as main_table
            WHERE 
                table_name = %s
                AND (
                    POSITION(
                        '/' || (SELECT name FROM {name_model} WHERE id = main_table.parent_id) || '/'
                        IN 
                        (SELECT path FROM {name_model} WHERE name = %s)
                    ) > 0
                    OR main_table.parent_id IS NULL
                )
        """
        return cls.objects.raw(query, [table, name])
    
    def save(self, *args, **kwargs):
        if self.parent is not None:
            parent_path = self.parent.path
            self.path = f'{parent_path}{self.name}/'
        else:
            self.path = f'/{self.name}/'

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
