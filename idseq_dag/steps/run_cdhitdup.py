import subprocess
from idseq_dag.engine.pipeline_step import PipelineStep
class PipelineStepRunCDHitDup(PipelineStep):
    def run(self):
        for f in self.output_files_local():
            subprocess.check_call("date > %s" % f, shell=True)