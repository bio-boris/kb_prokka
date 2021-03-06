
package us.kbase.kbprokka;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: AnnotateParams</p>
 * <pre>
 * Required parameters:
 *     object_ref - reference to Assembly or Genome object,
 *     output_workspace - output workspace name,
 *     output_genome_name - output object name,
 * Optional parameters (correspond to PROKKA command line arguments):
 *   --scientific_name Genome scientific name (default 'Unknown')
 *   --kingdom [X]     Annotation mode: Archaea|Bacteria|Mitochondria|Viruses (default 'Bacteria')
 *   --genus [X]       Genus name (triggers to use --usegenus)
 *   --gcode [N]       Genetic code / Translation table (set if --kingdom is set) (default '11')
 *   --metagenome      Improve gene predictions for highly fragmented genomes (default OFF)
 *   --rawproduct      Do not clean up /product annotation (default OFF)
 *   --fast            Fast mode - skip CDS /product searching (default OFF)
 *   --mincontiglen [N] Minimum contig size [NCBI needs 200] (default '1')
 *   --evalue [n.n]    Similarity e-value cut-off (default '1e-06')
 *   --rfam            Enable searching for ncRNAs with Infernal+Rfam (SLOW!) (default OFF)
 *   --norrna          Don't run rRNA search (default OFF)
 *   --notrna          Don't run tRNA search (default OFF)
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "object_ref",
    "output_workspace",
    "output_genome_name",
    "scientific_name",
    "kingdom",
    "genus",
    "gcode",
    "metagenome",
    "rawproduct",
    "fast",
    "mincontiglen",
    "evalue",
    "rfam",
    "norrna",
    "notrna"
})
public class AnnotateParams {

    @JsonProperty("object_ref")
    private String objectRef;
    @JsonProperty("output_workspace")
    private String outputWorkspace;
    @JsonProperty("output_genome_name")
    private String outputGenomeName;
    @JsonProperty("scientific_name")
    private String scientificName;
    @JsonProperty("kingdom")
    private String kingdom;
    @JsonProperty("genus")
    private String genus;
    @JsonProperty("gcode")
    private Long gcode;
    @JsonProperty("metagenome")
    private Long metagenome;
    @JsonProperty("rawproduct")
    private Long rawproduct;
    @JsonProperty("fast")
    private Long fast;
    @JsonProperty("mincontiglen")
    private Long mincontiglen;
    @JsonProperty("evalue")
    private String evalue;
    @JsonProperty("rfam")
    private Long rfam;
    @JsonProperty("norrna")
    private Long norrna;
    @JsonProperty("notrna")
    private Long notrna;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("object_ref")
    public String getObjectRef() {
        return objectRef;
    }

    @JsonProperty("object_ref")
    public void setObjectRef(String objectRef) {
        this.objectRef = objectRef;
    }

    public AnnotateParams withObjectRef(String objectRef) {
        this.objectRef = objectRef;
        return this;
    }

    @JsonProperty("output_workspace")
    public String getOutputWorkspace() {
        return outputWorkspace;
    }

    @JsonProperty("output_workspace")
    public void setOutputWorkspace(String outputWorkspace) {
        this.outputWorkspace = outputWorkspace;
    }

    public AnnotateParams withOutputWorkspace(String outputWorkspace) {
        this.outputWorkspace = outputWorkspace;
        return this;
    }

    @JsonProperty("output_genome_name")
    public String getOutputGenomeName() {
        return outputGenomeName;
    }

    @JsonProperty("output_genome_name")
    public void setOutputGenomeName(String outputGenomeName) {
        this.outputGenomeName = outputGenomeName;
    }

    public AnnotateParams withOutputGenomeName(String outputGenomeName) {
        this.outputGenomeName = outputGenomeName;
        return this;
    }

    @JsonProperty("scientific_name")
    public String getScientificName() {
        return scientificName;
    }

    @JsonProperty("scientific_name")
    public void setScientificName(String scientificName) {
        this.scientificName = scientificName;
    }

    public AnnotateParams withScientificName(String scientificName) {
        this.scientificName = scientificName;
        return this;
    }

    @JsonProperty("kingdom")
    public String getKingdom() {
        return kingdom;
    }

    @JsonProperty("kingdom")
    public void setKingdom(String kingdom) {
        this.kingdom = kingdom;
    }

    public AnnotateParams withKingdom(String kingdom) {
        this.kingdom = kingdom;
        return this;
    }

    @JsonProperty("genus")
    public String getGenus() {
        return genus;
    }

    @JsonProperty("genus")
    public void setGenus(String genus) {
        this.genus = genus;
    }

    public AnnotateParams withGenus(String genus) {
        this.genus = genus;
        return this;
    }

    @JsonProperty("gcode")
    public Long getGcode() {
        return gcode;
    }

    @JsonProperty("gcode")
    public void setGcode(Long gcode) {
        this.gcode = gcode;
    }

    public AnnotateParams withGcode(Long gcode) {
        this.gcode = gcode;
        return this;
    }

    @JsonProperty("metagenome")
    public Long getMetagenome() {
        return metagenome;
    }

    @JsonProperty("metagenome")
    public void setMetagenome(Long metagenome) {
        this.metagenome = metagenome;
    }

    public AnnotateParams withMetagenome(Long metagenome) {
        this.metagenome = metagenome;
        return this;
    }

    @JsonProperty("rawproduct")
    public Long getRawproduct() {
        return rawproduct;
    }

    @JsonProperty("rawproduct")
    public void setRawproduct(Long rawproduct) {
        this.rawproduct = rawproduct;
    }

    public AnnotateParams withRawproduct(Long rawproduct) {
        this.rawproduct = rawproduct;
        return this;
    }

    @JsonProperty("fast")
    public Long getFast() {
        return fast;
    }

    @JsonProperty("fast")
    public void setFast(Long fast) {
        this.fast = fast;
    }

    public AnnotateParams withFast(Long fast) {
        this.fast = fast;
        return this;
    }

    @JsonProperty("mincontiglen")
    public Long getMincontiglen() {
        return mincontiglen;
    }

    @JsonProperty("mincontiglen")
    public void setMincontiglen(Long mincontiglen) {
        this.mincontiglen = mincontiglen;
    }

    public AnnotateParams withMincontiglen(Long mincontiglen) {
        this.mincontiglen = mincontiglen;
        return this;
    }

    @JsonProperty("evalue")
    public String getEvalue() {
        return evalue;
    }

    @JsonProperty("evalue")
    public void setEvalue(String evalue) {
        this.evalue = evalue;
    }

    public AnnotateParams withEvalue(String evalue) {
        this.evalue = evalue;
        return this;
    }

    @JsonProperty("rfam")
    public Long getRfam() {
        return rfam;
    }

    @JsonProperty("rfam")
    public void setRfam(Long rfam) {
        this.rfam = rfam;
    }

    public AnnotateParams withRfam(Long rfam) {
        this.rfam = rfam;
        return this;
    }

    @JsonProperty("norrna")
    public Long getNorrna() {
        return norrna;
    }

    @JsonProperty("norrna")
    public void setNorrna(Long norrna) {
        this.norrna = norrna;
    }

    public AnnotateParams withNorrna(Long norrna) {
        this.norrna = norrna;
        return this;
    }

    @JsonProperty("notrna")
    public Long getNotrna() {
        return notrna;
    }

    @JsonProperty("notrna")
    public void setNotrna(Long notrna) {
        this.notrna = notrna;
    }

    public AnnotateParams withNotrna(Long notrna) {
        this.notrna = notrna;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((((((((((((((((((((((("AnnotateParams"+" [objectRef=")+ objectRef)+", outputWorkspace=")+ outputWorkspace)+", outputGenomeName=")+ outputGenomeName)+", scientificName=")+ scientificName)+", kingdom=")+ kingdom)+", genus=")+ genus)+", gcode=")+ gcode)+", metagenome=")+ metagenome)+", rawproduct=")+ rawproduct)+", fast=")+ fast)+", mincontiglen=")+ mincontiglen)+", evalue=")+ evalue)+", rfam=")+ rfam)+", norrna=")+ norrna)+", notrna=")+ notrna)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
