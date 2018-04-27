# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
from pprint import pformat
from kb_prokka.Util.ProkkaUtils import ProkkaUtils
from Workspace.WorkspaceClient import Workspace as workspaceService

#END_HEADER


class kb_prokka:
    '''
    Module Name:
    kb_prokka

    Module Description:
    A KBase module: kb_prokka
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/bio-boris/kb_prokka.git"
    GIT_COMMIT_HASH = "a06ff006d664e431bd27f4461699b6199e898af9"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        self.ws_client = workspaceService(config["workspace-url"])
        #END_CONSTRUCTOR
        pass


    def annotate(self, ctx, params):
        """
        :param params: instance of type "AnnotateParams" (Required
           parameters: object_ref - reference to Assembly or Genome object,
           output_workspace - output workspace name, output_genome_name -
           output object name, Optional parameters (correspond to PROKKA
           command line arguments): --scientific_name Genome scientific name
           (default 'Unknown') --kingdom [X]     Annotation mode:
           Archaea|Bacteria|Mitochondria|Viruses (default 'Bacteria') --genus
           [X]       Genus name (triggers to use --usegenus) --gcode [N]     
           Genetic code / Translation table (set if --kingdom is set)
           (default '11') --metagenome      Improve gene predictions for
           highly fragmented genomes (default OFF) --rawproduct      Do not
           clean up /product annotation (default OFF) --fast            Fast
           mode - skip CDS /product searching (default OFF) --mincontiglen
           [N] Minimum contig size [NCBI needs 200] (default '1') --evalue
           [n.n]    Similarity e-value cut-off (default '1e-06') --rfam      
           Enable searching for ncRNAs with Infernal+Rfam (SLOW!) (default
           OFF) --norrna          Don't run rRNA search (default OFF)
           --notrna          Don't run tRNA search (default OFF)) ->
           structure: parameter "object_ref" of type "data_obj_ref"
           (Reference to an Assembly or Genome object in the workspace @id ws
           KBaseGenomeAnnotations.Assembly @id ws KBaseGenomes.Genome),
           parameter "output_workspace" of String, parameter
           "output_genome_name" of String, parameter "scientific_name" of
           String, parameter "kingdom" of String, parameter "genus" of
           String, parameter "gcode" of Long, parameter "metagenome" of type
           "boolean" (A boolean. 0 = false, anything else = true.), parameter
           "rawproduct" of type "boolean" (A boolean. 0 = false, anything
           else = true.), parameter "fast" of type "boolean" (A boolean. 0 =
           false, anything else = true.), parameter "mincontiglen" of Long,
           parameter "evalue" of String, parameter "rfam" of type "boolean"
           (A boolean. 0 = false, anything else = true.), parameter "norrna"
           of type "boolean" (A boolean. 0 = false, anything else = true.),
           parameter "notrna" of type "boolean" (A boolean. 0 = false,
           anything else = true.)
        :returns: instance of type "AnnotateOutput" -> structure: parameter
           "output_genome_ref" of type "genome_ref" (Reference to an Genome
           object in the workspace @id ws KBaseGenomes.Genome), parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN annotate
        print("Input parameters: " + pformat(params))
        object_ref = params['object_ref']
        object_info = self.ws_client.get_object_info_new({"objects": [{"ref": object_ref}],
                                                           "includeMetadata": 1})[0]
        object_type = object_info[2]

        self.config['ctx'] = ctx
        prokka_runner = ProkkaUtils(self.config)

        if "KBaseGenomeAnnotations.Assembly" in object_type:
            return [prokka_runner.annotate_assembly(params, object_info)]
        elif "KBaseGenomes.Genome" in object_type:
            return [prokka_runner.annotate_genome(params)]
        else:
            raise Exception("Unsupported type" + object_type)
        #END annotate

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method annotate return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {"state": "OK",
                     "message": "",
                     "version": self.VERSION,
                     "git_url": self.GIT_URL,
                     "git_commit_hash": self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
