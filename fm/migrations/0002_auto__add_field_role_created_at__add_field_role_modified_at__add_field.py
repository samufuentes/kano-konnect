# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Role.created_at'
        db.add_column(u'fm_role', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Role.modified_at'
        db.add_column(u'fm_role', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Role.deleted_on'
        db.add_column(u'fm_role', 'deleted_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'FacilityImage.created_at'
        db.add_column(u'fm_facilityimage', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'FacilityImage.modified_at'
        db.add_column(u'fm_facilityimage', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'FacilityImage.deleted_on'
        db.add_column(u'fm_facilityimage', 'deleted_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Facility.created_at'
        db.add_column(u'fm_facility', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Facility.modified_at'
        db.add_column(u'fm_facility', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Facility.deleted_on'
        db.add_column(u'fm_facility', 'deleted_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Area.created_at'
        db.add_column(u'fm_area', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Area.modified_at'
        db.add_column(u'fm_area', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Area.deleted_on'
        db.add_column(u'fm_area', 'deleted_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Contact.created_at'
        db.add_column(u'fm_contact', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Contact.modified_at'
        db.add_column(u'fm_contact', 'modified_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 8, 4, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Contact.deleted_on'
        db.add_column(u'fm_contact', 'deleted_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Role.created_at'
        db.delete_column(u'fm_role', 'created_at')

        # Deleting field 'Role.modified_at'
        db.delete_column(u'fm_role', 'modified_at')

        # Deleting field 'Role.deleted_on'
        db.delete_column(u'fm_role', 'deleted_on')

        # Deleting field 'FacilityImage.created_at'
        db.delete_column(u'fm_facilityimage', 'created_at')

        # Deleting field 'FacilityImage.modified_at'
        db.delete_column(u'fm_facilityimage', 'modified_at')

        # Deleting field 'FacilityImage.deleted_on'
        db.delete_column(u'fm_facilityimage', 'deleted_on')

        # Deleting field 'Facility.created_at'
        db.delete_column(u'fm_facility', 'created_at')

        # Deleting field 'Facility.modified_at'
        db.delete_column(u'fm_facility', 'modified_at')

        # Deleting field 'Facility.deleted_on'
        db.delete_column(u'fm_facility', 'deleted_on')

        # Deleting field 'Area.created_at'
        db.delete_column(u'fm_area', 'created_at')

        # Deleting field 'Area.modified_at'
        db.delete_column(u'fm_area', 'modified_at')

        # Deleting field 'Area.deleted_on'
        db.delete_column(u'fm_area', 'deleted_on')

        # Deleting field 'Contact.created_at'
        db.delete_column(u'fm_contact', 'created_at')

        # Deleting field 'Contact.modified_at'
        db.delete_column(u'fm_contact', 'modified_at')

        # Deleting field 'Contact.deleted_on'
        db.delete_column(u'fm_contact', 'deleted_on')


    models = {
        u'fm.area': {
            'Meta': {'object_name': 'Area'},
            'area_name': ('django.db.models.fields.TextField', [], {}),
            'area_parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_children'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': u"orm['fm.Area']", 'blank': 'True', 'null': 'True'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'fm.contact': {
            'Meta': {'object_name': 'Contact'},
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
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deleted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fm.Facility']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'fm.role': {
            'Meta': {'object_name': 'Role'},
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