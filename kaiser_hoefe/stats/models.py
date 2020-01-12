# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amt(models.Model):
    amt = models.CharField(db_column='Amt', primary_key=True, max_length=40)  # Field name made lowercase.
    hofamt = models.CharField(db_column='Hofamt', max_length=50)  # Field name made lowercase.
    gnd = models.CharField(db_column='GND', max_length=10)  # Field name made lowercase.
    rang = models.PositiveIntegerField(db_column='Rang')  # Field name made lowercase.
    aktiv = models.PositiveIntegerField(db_column='Aktiv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'amt'


class Archiv(models.Model):
    sigle = models.CharField(db_column='Sigle', primary_key=True, max_length=50)  # Field name made lowercase.
    bestand = models.CharField(db_column='Bestand', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'archiv'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Beziehung(models.Model):
    f41x = models.OneToOneField('Person', models.DO_NOTHING, db_column='F41X', primary_key=True, related_name='parent_or_husband')  # Field name made lowercase.
    art = models.IntegerField(db_column='Art')  # Field name made lowercase.
    f41y = models.ForeignKey('Person', models.DO_NOTHING, db_column='F41Y', related_name='child_or_wife')  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'beziehung'
        unique_together = (('f41x', 'f41y'),)


class Bild(models.Model):
    f41 = models.OneToOneField('Person', models.DO_NOTHING, db_column='F41', primary_key=True)  # Field name made lowercase.
    credits = models.CharField(db_column='Credits', max_length=200)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=255)  # Field name made lowercase.
    art = models.CharField(db_column='Art', max_length=1)  # Field name made lowercase.
    cache = models.PositiveIntegerField(db_column='Cache')  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bild'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hofstaat(models.Model):
    hofherr = models.CharField(db_column='Hofherr', primary_key=True, max_length=4)  # Field name made lowercase.
    f41 = models.ForeignKey('Person', models.DO_NOTHING, db_column='F41', blank=True, null=True)  # Field name made lowercase.
    bezeichnung = models.CharField(db_column='Bezeichnung', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hofstaat'


class Konkordanz(models.Model):
    f41 = models.OneToOneField('Person', models.DO_NOTHING, db_column='F41', primary_key=True)  # Field name made lowercase.
    referenz = models.CharField(db_column='Referenz', max_length=6)  # Field name made lowercase.
    f45 = models.CharField(db_column='F45', max_length=90)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'konkordanz'
        unique_together = (('f41', 'referenz', 'f45'), ('referenz', 'f45'),)


class Literatur(models.Model):
    literatur = models.SmallAutoField(db_column='Literatur', primary_key=True)  # Field name made lowercase.
    jahr = models.PositiveSmallIntegerField(db_column='Jahr')  # Field name made lowercase.
    titelaufnahme = models.TextField(db_column='Titelaufnahme')  # Field name made lowercase.
    signatur = models.CharField(db_column='Signatur', max_length=100)  # Field name made lowercase.
    credits = models.CharField(db_column='Credits', max_length=100)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200)  # Field name made lowercase.
    k = models.CharField(db_column='K', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'literatur'


class Nachweis(models.Model):
    f41 = models.OneToOneField('Person', models.DO_NOTHING, db_column='F41', primary_key=True)  # Field name made lowercase.
    literatur = models.ForeignKey(Literatur, models.DO_NOTHING, db_column='Literatur')  # Field name made lowercase.
    seiten = models.CharField(db_column='Seiten', max_length=20)  # Field name made lowercase.
    kommentar = models.CharField(db_column='Kommentar', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nachweis'
        unique_together = (('f41', 'literatur', 'seiten'),)


class Ort(models.Model):
    b = models.DecimalField(db_column='B', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    l = models.DecimalField(db_column='L', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    y = models.CharField(db_column='Y', max_length=2)  # Field name made lowercase.
    ort = models.CharField(db_column='Ort', primary_key=True, max_length=60)  # Field name made lowercase.
    la = models.CharField(max_length=60)
    en = models.CharField(max_length=60)
    fr = models.CharField(max_length=60)
    nl = models.CharField(max_length=60)
    es = models.CharField(max_length=60)
    it = models.CharField(max_length=60)
    ro = models.CharField(max_length=60)
    pl = models.CharField(max_length=60)
    cs = models.CharField(max_length=60)
    sk = models.CharField(max_length=60)
    hu = models.CharField(max_length=60)
    si = models.CharField(max_length=60)
    hr = models.CharField(max_length=60)
    xy = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'ort'


class Person(models.Model):
    f41 = models.SmallAutoField(db_column='F41', primary_key=True)  # Field name made lowercase.
    zlabel = models.CharField(db_column='ZLabel', max_length=100)  # Field name made lowercase.
    f13 = models.CharField(db_column='F13', max_length=20)  # Field name made lowercase.
    f15 = models.ForeignKey(Ort, models.DO_NOTHING, db_column='F15', related_name='birthplace')  # Field name made lowercase.
    f14 = models.CharField(db_column='F14', max_length=20)  # Field name made lowercase.
    f16 = models.CharField(db_column='F16', max_length=120)  # Field name made lowercase.
    f24 = models.CharField(db_column='F24', max_length=1)  # Field name made lowercase.
    kommentar = models.TextField(db_column='Kommentar')  # Field name made lowercase.
    f17 = models.ForeignKey(Ort, models.DO_NOTHING, db_column='F17', blank=True, null=True, related_name='place_of_death')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person'

    def __str__(self):
        return str(self.zlabel)


class Quelle(models.Model):
    quelle = models.CharField(db_column='Quelle', primary_key=True, max_length=12)  # Field name made lowercase.
    signatur = models.CharField(db_column='Signatur', max_length=48)  # Field name made lowercase.
    paginierung = models.CharField(db_column='Paginierung', max_length=4)  # Field name made lowercase.
    kurztitel = models.CharField(db_column='Kurztitel', max_length=60)  # Field name made lowercase.
    laufzeit = models.CharField(db_column='Laufzeit', max_length=9)  # Field name made lowercase.
    incipit = models.TextField(db_column='Incipit')  # Field name made lowercase.
    beschreibung = models.TextField(db_column='Beschreibung')  # Field name made lowercase.
    kommentar = models.TextField(db_column='Kommentar')  # Field name made lowercase.
    archivplan = models.CharField(db_column='Archivplan', max_length=100)  # Field name made lowercase.
    editionen = models.CharField(db_column='Editionen', max_length=120)  # Field name made lowercase.
    restrict = models.PositiveIntegerField(db_column='Restrict')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quelle'


class Scan(models.Model):
    spalte = models.SmallAutoField(db_column='Spalte', primary_key=True)  # Field name made lowercase.
    stapel = models.CharField(db_column='Stapel', max_length=90)  # Field name made lowercase.
    dateiname = models.CharField(db_column='Dateiname', max_length=30)  # Field name made lowercase.
    quelle = models.ForeignKey(Quelle, models.DO_NOTHING, db_column='Quelle')  # Field name made lowercase.
    seite = models.CharField(db_column='Seite', max_length=4)  # Field name made lowercase.
    x = models.PositiveSmallIntegerField(db_column='X')  # Field name made lowercase.
    y = models.PositiveSmallIntegerField(db_column='Y')  # Field name made lowercase.
    inserted_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scan'


class Schema(models.Model):
    c = models.CharField(db_column='C', primary_key=True, max_length=16)  # Field name made lowercase.
    amt = models.CharField(db_column='Amt', unique=True, max_length=60)  # Field name made lowercase.
    beschreibung = models.TextField(db_column='Beschreibung')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schema'


class Segment(models.Model):
    eintrag = models.OneToOneField('Transkriptionen', models.DO_NOTHING, db_column='Eintrag', primary_key=True)  # Field name made lowercase.
    x = models.PositiveSmallIntegerField(db_column='X')  # Field name made lowercase.
    y = models.PositiveSmallIntegerField(db_column='Y')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'segment'


class Transkriptionen(models.Model):
    eintrag = models.AutoField(db_column='Eintrag', primary_key=True)  # Field name made lowercase.
    quelle = models.ForeignKey(Quelle, models.DO_NOTHING, db_column='Quelle')  # Field name made lowercase.
    seite = models.CharField(db_column='Seite', max_length=4)  # Field name made lowercase.
    amt = models.ForeignKey(Amt, models.DO_NOTHING, db_column='Amt')  # Field name made lowercase.
    hofherr = models.ForeignKey(Hofstaat, models.DO_NOTHING, db_column='Hofherr')  # Field name made lowercase.
    laufnr = models.CharField(db_column='Laufnr', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    dienstbeginn = models.CharField(db_column='Dienstbeginn', max_length=20)  # Field name made lowercase.
    erwaehnung = models.CharField(db_column='Erwaehnung', max_length=20)  # Field name made lowercase.
    abraitung = models.CharField(db_column='Abraitung', max_length=20)  # Field name made lowercase.
    promotion = models.CharField(db_column='Promotion', max_length=20)  # Field name made lowercase.
    erstaufnahme = models.CharField(db_column='Erstaufnahme', max_length=3)  # Field name made lowercase.
    quellenkommentar = models.TextField(db_column='Quellenkommentar')  # Field name made lowercase.
    bearbeiterkommentar = models.TextField(db_column='Bearbeiterkommentar')  # Field name made lowercase.
    anmerkung = models.CharField(db_column='Anmerkung', max_length=200)  # Field name made lowercase.
    sort = models.CharField(db_column='Sort', max_length=20)  # Field name made lowercase.
    f41 = models.ForeignKey(Person, models.DO_NOTHING, db_column='F41', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transkriptionen'


class Treffer(models.Model):
    f41 = models.OneToOneField(Person, models.DO_NOTHING, db_column='F41', primary_key=True)  # Field name made lowercase.
    katalog = models.CharField(db_column='Katalog', max_length=6)  # Field name made lowercase.
    treffer = models.PositiveSmallIntegerField(db_column='Treffer')  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'treffer'
        unique_together = (('f41', 'katalog', 'url'),)
