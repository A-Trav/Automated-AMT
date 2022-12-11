import pytest

from Test.fixtures import app
from ScheduledTask.task import importer_task
from Utils.startup_tasks import import_snomed_csv
from Model.amt import Amt, Snomed
from Service.version import get_version

def test_scheduled_task(app):
    assert len(Amt.query.all()) == 0
    assert get_version() == None

    importer_task(app)
    assert len(Amt.query.all()) != 0
    assert get_version() != None

def test_snomed_import(app):
    assert len(Snomed.query.all()) == 0

    import_snomed_csv(app)
    
    assert len(Snomed.query.all()) != 0

