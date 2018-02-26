# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from kb_prokka.kb_prokkaImpl import kb_prokka
from kb_prokka.kb_prokkaServer import MethodContext
from kb_prokka.authclient import KBaseAuth as _KBaseAuth
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from DataFileUtil.DataFileUtilClient import DataFileUtil

class kb_prokkaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('kb_prokka'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'kb_prokka',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = kb_prokka(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_kb_prokka_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx


    def XtestUpload(self):
        from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil
        gfu = GenomeFileUtil(os.environ['SDK_CALLBACK_URL'])
        data = {'id': 'id', 'scientific_name': 'scientific_name', 'domain': 'domain',
                'genetic_code': 0}
        info = gfu.save_one_genome({'workspace': self.getWsName(),
                                          'name': 'IAMAGSAGSAGA',
                                          'data': data })

        dfu = DataFileUtil(os.environ['SDK_CALLBACK_URL'])
        # workspace_id = dfu.ws_name_to_id(self.getWsName())

        # dfu_save_params = {'id': workspace_id,
        #                    'objects': [{'type': 'KBaseGenomes.Genome',
        #                                 'data': data,
        #                                 'name': 'name',
        #                                 }]}
        #
        # dfu_oi = dfu.save_objects(dfu_save_params)[0]

        pprint(info)


    def testReAnnotateGenome(self):
        self.getImpl().annotate(self.getContext(),
                                {'object_ref': '12972/5/1',
                                 'output_workspace': self.getWsName(),
                                 'output_genome_name': 'genome_name',
                                 'evalue': None,
                                 'fast': 0,
                                 'gcode': 0,
                                 'genus': 'genus',
                                 'kingdom': 'Bacteria',
                                 'metagenome': 0,
                                 'mincontiglen': 1,
                                 'norrna': 0,
                                 'notrna': 0,
                                 'rawproduct': 0,
                                 'rfam': 1,
                                 'scientific_name': 'Super : diper - name;'
                                 })

    def XtestAnnotateAssembly(self):
        self.getImpl().annotate(self.getContext(),
                                {'object_ref': '12972/3/1',
                                 'output_workspace': self.getWsName(),
                                 'output_genome_name': 'genome_name',
                                 'evalue': None,
                                 'fast': 0,
                                 'gcode': 0,
                                 'genus': 'genus',
                                 'kingdom': 'Bacteria',
                                 'metagenome': 0,
                                 'mincontiglen': 1,
                                 'norrna': 0,
                                 'notrna': 0,
                                 'rawproduct': 0,
                                 'rfam': 1,
                                 'scientific_name': 'Super : diper - name;'
                                 })



    def Xtest_annotate_contigs_too_big(self):
        """
        simulate a metagenome contig file
        """
        # Create a fake assembly with lots of contigs
        assembly_file_name = "bogus.fna"  #"AP009048.fna"
        assembly_temp_file = os.path.join("/kb/module/work/tmp", assembly_file_name)
        with open(assembly_temp_file, 'w') as f:
            for i in range(1,30002):
                f.write('> contig_%d\n' % i)
                f.write('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC\n')

        assembly_name = 'Assembly.2'
        au = AssemblyUtil(os.environ['SDK_CALLBACK_URL'], token=self.getContext()['token'])
        assembly_ref = au.save_assembly_from_fasta({'file': {'path': assembly_temp_file},
                                                    'workspace_name': self.getWsName(),
                                                    'assembly_name': assembly_name})
        genome_name = "Genome.1"
        # This should fail with an error
        with self.assertRaises(ValueError):
            result = self.getImpl().annotate(self.getContext(),
                                                     {'assembly_ref': assembly_ref,
                                                      'output_workspace': self.getWsName(),
                                                      'output_genome_name': genome_name,
                                                      'evalue': None,
                                                      'fast': 0,
                                                      'gcode': 0,
                                                      'genus': 'genus',
                                                      'kingdom': 'Bacteria',
                                                      'metagenome': 0,
                                                      'mincontiglen': 1,
                                                      'norrna': 0,
                                                      'notrna': 0,
                                                      'rawproduct': 0,
                                                      'rfam': 1,
                                                      'scientific_name': 'Super : diper - name;'
                                                      })
