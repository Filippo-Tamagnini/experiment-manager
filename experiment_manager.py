# -*- coding: utf-8 -*-
"""
Experiment manager

Some code to help store experimental results
How to use:
1) create a Manager object specifying a folder to put results in, 
    field names to put in the summary and key=value pairs of metadata information
2) add experiment results to the summary file by calling new_experiment(key = value)
    with keys corresponding to the field names defined in point 1
2.1) the  new_experiment method returns a folder name to put additional files in

@author: Filippo Tamagnini
"""
import csv
import os
import time

class Manager():
    def __init__(self, root, *fields, **metadata):
        self.root = root
        self.summary_fields = [f for f in fields]
          
        # Setup the root folder and the summary file
        try:
            os.mkdir(self.root)
            with open(self.root + "/summary.csv", "x",newline = "") as FID:
                writer = csv.writer(FID, dialect = "excel")
                writer.writerow(["expid"] + self.summary_fields)
        except FileExistsError:
            None
        
        self._save_metadata(metadata)
                    
    def new_experiment(self, **summary):
        expid = str(time.time())
        row = [expid] + [summary[key] for key in self.summary_fields]
        with open(self.root + "/summary.csv", "a",newline = "") as FID:
            writer = csv.writer(FID, dialect = "excel")
            writer.writerow(row)
        exp_dir = self.root + "/" + expid
        os.mkdir(exp_dir)
        return exp_dir    
    
    def _save_metadata(self, metadata_dict):
        with open(self.root + "/metadata.csv", "x", newline = "") as FID:
            writer_metadata = csv.writer(FID, dialect = "excel")
            for key, value in metadata_dict.items():
                writer_metadata.writerow([key, value])