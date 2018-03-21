# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests
import shutil

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from kb_prokka.kb_prokkaImpl import kb_prokka
from kb_prokka.kb_prokkaServer import MethodContext
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from kb_prokka.authclient import KBaseAuth as _KBaseAuth
from AssemblySequenceAPI.AssemblySequenceAPIClient import AssemblySequenceAPI
from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil
from DataFileUtil.DataFileUtilClient import DataFileUtil

from kb_prokka.genome_object_client import add_features




class ProkkaAnnotationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config_file = environ.get("KB_DEPLOYMENT_CONFIG", None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items("kb_prokka"):
            cls.cfg[nameval[0]] = nameval[1]
        # Token validation
        token = environ.get("KB_AUTH_TOKEN", None)
        authServiceUrl = cls.cfg.get("auth-service-url",
                "https://kbase.us/services/authorization/Sessions/Login")
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don"t call any logging methods on the context object,
        # it"ll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({"token": token,
                        "user_id": user_id,
                        "provenance": [
                            {"service": "ProkkaAnnotation",
                             "method": "please_never_use_it_in_production",
                             "method_params": []
                             }],
                        "authenticated": 1})
        cls.wsURL = cls.cfg["workspace-url"]
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = kb_prokka(cls.cfg)


    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "wsName"):
            cls.wsClient.delete_workspace({"workspace": cls.wsName})
            print("Test workspace was deleted")

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, "wsName"):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_ProkkaAnnotation_" + str(suffix)
        ret = self.getWsClient().create_workspace({"workspace": wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx


  #  def testGenomeOntologyEventsField(self):
  #      testwith ontology events
  #      test without


    def Xtest_modify_old_genome(self):
        self.callback_url = os.environ["SDK_CALLBACK_URL"]
        self.gfu = GenomeFileUtil(self.callback_url)
        self.dfu = DataFileUtil(self.callback_url)
        old_genome = "30045/15/1"

        new_genome = "30045/14/1"
        genome_name = 'OldRhodo'
        genome_data = self.dfu.get_objects({"object_refs": [new_genome]})["data"][0]

        sso_1 = {"id" : "1",
                 "evidence": [],
                 "term_name": "1",
                 "ontology_ref": "1",
                 "term_lineage": []}

        sso_2 = {"id": "2",
                 "evidence": [],
                 "term_name": "2",
                 "ontology_ref": "2",
                 "term_lineage": []}

        sso_terms = { 'SSO1' : sso_1  , 'SSO2' : sso_2 }

        for i,item in enumerate(genome_data['data']['features']):
           genome_data['data']['features'][i]['ontology_terms'] = {"SSO": sso_terms}



        info = self.gfu.save_one_genome({"workspace": self.getWsName(),
                                         "name": genome_name,
                                         "data": genome_data["data"],
                                         "provenance": self.ctx.provenance()})["info"]




    def test_reannotate_new_genome(self):
        genome_ref = '30045/14/1'
        genome_name = 'NewRhodo'

        result = self.getImpl().annotate(self.getContext(),
                                         {"object_ref": genome_ref,
                                          "output_workspace": self.getWsName(),
                                          "output_genome_name": genome_name,
                                          "evalue": None,
                                          "fast": 0,
                                          "gcode": 0,
                                          "genus": "genus",
                                          "kingdom": "Bacteria",
                                          "metagenome": 0,
                                          "mincontiglen": 1,
                                          "norrna": 0,
                                          "notrna": 0,
                                          "rawproduct": 0,
                                          "rfam": 1,
                                          "scientific_name": "RhodoBacter"
                                          })[0]

    def Xtest_reannotate_old_genome(self):
        genome_ref = '30045/15/1'
        genome_name = 'OldRhodo'

        result = self.getImpl().annotate(self.getContext(),
                                         {"object_ref": genome_ref,
                                          "output_workspace": self.getWsName(),
                                          "output_genome_name": genome_name,
                                          "evalue": None,
                                          "fast": 0,
                                          "gcode": 0,
                                          "genus": "genus",
                                          "kingdom": "Bacteria",
                                          "metagenome": 0,
                                          "mincontiglen": 1,
                                          "norrna": 0,
                                          "notrna": 0,
                                          "rawproduct": 0,
                                          "rfam": 1,
                                          "scientific_name": "RhodoBacter"
                                          })[0]


