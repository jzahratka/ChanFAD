"""
Definition of models.
"""

from django.db import models
from django.urls import reverse


# Create your models here.

class Channel(models.Model):
    pdb = models.CharField(max_length=4, primary_key=True, help_text="A 4-character PDB ID. This acts as the primary key.")
    species = models.CharField(max_length=50, help_text="Genus and species")
    geneName = models.CharField(max_length=10, help_text="Use the gene abbreviation (e.g. TRPV1)")
    description = models.CharField(max_length=100, help_text="This is the long form (e.g. Transient receptor potential, vanilloid 1)")
    ion = models.CharField(max_length=3, help_text="Use Na, K, Ca, Cl, H for individual ions, CAT for cations, ANI for anions, UNK for unknown")
    icn3d = models.TextField(max_length=5000, help_text="The FULL-LENGTH ICn3D generated link. Maximum 4000 characters.")
    submitter = models.CharField(max_length=50, help_text="First initial, period, last name")
    uniprot = models.CharField(max_length=6, help_text="Six-character UniProt identifier. Used for linking to the channels' UniProt page.")
    channelpedia = models.CharField(max_length=1000, help_text="Channelpedia link, if applicable. Leave blank if there is no Channelpedia entry present.")
    kegg = models.CharField(max_length=10, null=True, blank=True, help_text="KEGG Pathway Reference number (e.g., K04857), null ok")
    iuphar = models.TextField(max_length=255, null=True, blank=True, help_text="IUPHAR ion channel database LINK. Not available for all channels, null ok")
    reference = models.CharField(max_length=255, null=True, blank=True, help_text="DOI for primary reference corresponding to PDB model. null ok")
    fasta = models.TextField(max_length=5000, null=True, blank=True, help_text="FASTA sequence for the primary channel subunit. null ok")
    featureset = models.TextField(max_length=5000, null=True, blank=True, help_text="Array of features in text for visualizing annotations. null ok")
    dateSubmission = models.DateTimeField()

    def __str__(self):
        return self.pdb

    def get_absolute_url(self):
        return reverse('channel-entry', args=[str(self.pdb)])

class Annotation(models.Model):
    domainIndex = models.IntegerField(primary_key = True, help_text="Internal index number for rows. Used as the primary key.")
    pdb = models.CharField(max_length=4, help_text="A 4-character PDB ID. Should match the PDB found in the Channel class for a given instance.")
    domain = models.CharField(max_length=100, help_text="Functional annotation domain name.")
    chain = models.CharField(max_length=3, help_text="PDB Chain where the domain or motif is found.")
    residues = models.CharField(max_length=15, help_text="Amino acid residues where the domain is located. This is parsed as a text field, and should follow the format \"20-40\".")
    notes = models.TextField(max_length=1000, help_text="Specific information that is potentially relevant to the domain or motif.")
    citation = models.TextField(max_length=1000, help_text="The citation where annotated information was found. DOI URLs are preferred.")

    def __str__(self):
        return self.pdb
