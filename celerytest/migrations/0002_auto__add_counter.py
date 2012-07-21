# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Counter'
        db.create_table('celerytest_counter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.BigIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('celerytest', ['Counter'])


    def backwards(self, orm):
        # Deleting model 'Counter'
        db.delete_table('celerytest_counter')


    models = {
        'celerytest.counter': {
            'Meta': {'object_name': 'Counter'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['celerytest']