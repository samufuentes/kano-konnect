# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table(u'fm_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area_name', self.gf('django.db.models.fields.TextField')()),
            ('area_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('area_parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_children', on_delete=models.SET_NULL, default=None, to=orm['fm.Area'], blank=True, null=True)),
        ))
        db.send_create_signal(u'fm', ['Area'])

        # Adding model 'Facility'
        db.create_table(u'fm_facility', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility_name', self.gf('django.db.models.fields.TextField')()),
            ('facility_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('facility_status', self.gf('django.db.models.fields.TextField')()),
            ('facility_area', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_facilities', on_delete=models.SET_NULL, default=None, to=orm['fm.Area'], blank=True, null=True)),
            ('json', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'fm', ['Facility'])

        # Adding model 'FacilityImage'
        db.create_table(u'fm_facilityimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fm.Facility'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'fm', ['FacilityImage'])

        # Adding model 'Contact'
        db.create_table(u'fm_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact_name', self.gf('django.db.models.fields.TextField')()),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('json', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'fm', ['Contact'])

        # Adding model 'Role'
        db.create_table(u'fm_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('role_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('role_contact', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='contact_roles', null=True, to=orm['fm.Contact'])),
            ('role_facility', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='facility_roles', null=True, to=orm['fm.Facility'])),
        ))
        db.send_create_signal(u'fm', ['Role'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table(u'fm_area')

        # Deleting model 'Facility'
        db.delete_table(u'fm_facility')

        # Deleting model 'FacilityImage'
        db.delete_table(u'fm_facilityimage')

        # Deleting model 'Contact'
        db.delete_table(u'fm_contact')

        # Deleting model 'Role'
        db.delete_table(u'fm_role')


    models = {
        u'fm.area': {
            'Meta': {'object_name': 'Area'},
            'area_name': ('django.db.models.fields.TextField', [], {}),
            'area_parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_children'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': u"orm['fm.Area']", 'blank': 'True', 'null': 'True'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'fm.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_name': ('django.db.models.fields.TextField', [], {}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fm.facility': {
            'Meta': {'object_name': 'Facility'},
            'facility_area': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_facilities'", 'on_delete': 'models.SET_NULL', 'default': 'None', 'to': u"orm['fm.Area']", 'blank': 'True', 'null': 'True'}),
            'facility_name': ('django.db.models.fields.TextField', [], {}),
            'facility_status': ('django.db.models.fields.TextField', [], {}),
            'facility_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fm.facilityimage': {
            'Meta': {'object_name': 'FacilityImage'},
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fm.Facility']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'fm.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role_contact': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'contact_roles'", 'null': 'True', 'to': u"orm['fm.Contact']"}),
            'role_facility': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'facility_roles'", 'null': 'True', 'to': u"orm['fm.Facility']"}),
            'role_name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['fm']