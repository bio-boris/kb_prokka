# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_prokka(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def annotate(self, params, context=None):
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
        return self._client.call_method(
            'kb_prokka.annotate',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_prokka.status',
                                        [], self._service_ver, context)
