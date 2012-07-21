# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Counter.date'
        db.delete_column('celerytest_counter', 'date')


    def backwards(self, orm):
        # Adding field 'Counter.date'
        db.add_column('celerytest_counter', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 15, 0, 0)),
                      keep_default=False)


    models = {
        'celerytest.counter': {
            'Meta': {'object_name': 'Counter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['celerytest']