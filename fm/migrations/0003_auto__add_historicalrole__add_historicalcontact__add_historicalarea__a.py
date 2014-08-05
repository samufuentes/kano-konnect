# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HistoricalRole'
        db.create_table(u'fm_historicalrole', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('deleted_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('changed_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('role_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('role_contact_id', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, db_index=True, blank=True)),
            ('role_facility_id', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, db_index=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'fm', ['HistoricalRole'])

        # Adding model 'HistoricalContact'
        db.create_table(u'fm_historicalcontact', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('deleted_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('changed_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.TextField')()),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('json', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'fm', ['HistoricalContact'])

        # Adding model 'HistoricalArea'
        db.create_table(u'fm_historicalarea', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('deleted_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('changed_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('area_name', self.gf('django.db.models.fields.TextField')()),
            ('area_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('area_parent_id', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, db_index=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'fm', ['HistoricalArea'])

        # Adding model 'HistoricalFacility'
        db.create_table(u'fm_historicalfacility', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('deleted_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('changed_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('facility_name', self.gf('django.db.models.fields.TextField')()),
            ('facility_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('facility_status', self.gf('django.db.models.fields.TextField')()),
            ('facility_area_id', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, db_index=True, blank=True)),
            ('json', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'fm', ['HistoricalFacility'])

        # Adding field 'Role.changed_by'
        db.add_column(u'fm_role', 'changed_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'FacilityImage.changed_by'
        db.add_column(u'fm_facilityimage', 'changed_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'Facility.changed_by'
        db.add_column(u'fm_facility', 'changed_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'Area.changed_by'
        db.add_column(u'fm_area', 'changed_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'Contact.changed_by'
        db.add_column(u'fm_contact', 'changed_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'HistoricalRole'
        db.delete_table(u'fm_historicalrole')

        # Deleting model 'HistoricalContact'
        db.delete_table(u'fm_historicalcontact')

        # Deleting model 'HistoricalArea'
        db.delete_table(u'fm_historicalarea')

        # Deleting model 'HistoricalFacility'
        db.delete_table(u'fm_historicalfacility')

        # Deleting field 'Role.changed_by'
        db.delete_column(u'fm_role', 'changed_by_id')

        # Deleting field 'FacilityImage.changed_by'
        db.delete_column(u'fm_facilityimage', 'changed_by_id')

        # Deleting field 'Facility.changed_by'
        db.delete_column(u'fm_facility', 'changed_by_id')

        # Deleting field 'Area.changed_by'
        db.delete_column(u'fm_area', 'changed_by_id')

        # Deleting field 'Contact.changed_by'
        db.delete_column(u'fm_contact', 'changed_by_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fm.area': {
            'Meta': {'object_name': 'Area'},
            'area_name': ('django.db.models.fields.TextField', [], {}),
            'area_parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_children'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': u"orm['fm.Area']", 'blank': 'True', 'null': 'True'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'fm.contact': {
            'Meta': {'object_name': 'Contact'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.TextField', [], {}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'fm.facility': {
            'Meta': {'object_name': 'Facility'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facility_area': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_facilities'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': u"orm['fm.Area']", 'blank': 'True', 'null': 'True'}),
            'facility_name': ('django.db.models.fields.TextField', [], {}),
            'facility_status': ('django.db.models.fields.TextField', [], {}),
            'facility_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'fm.facilityimage': {
            'Meta': {'object_name': 'FacilityImage'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fm.Facility']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'fm.historicalarea': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalArea'},
            'area_name': ('django.db.models.fields.TextField', [], {}),
            'area_parent_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        u'fm.historicalcontact': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalContact'},
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.TextField', [], {}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        u'fm.historicalfacility': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalFacility'},
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facility_area_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'facility_name': ('django.db.models.fields.TextField', [], {}),
            'facility_status': ('django.db.models.fields.TextField', [], {}),
            'facility_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        u'fm.historicalrole': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalRole'},
            'changed_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'role_contact_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'role_facility_id': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'fm.role': {
            'Meta': {'object_name': 'Role'},
            'changed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'role_contact': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'contact_roles'", 'null': 'True', 'to': u"orm['fm.Contact']"}),
            'role_facility': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'facility_roles'", 'null': 'True', 'to': u"orm['fm.Facility']"}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['fm']