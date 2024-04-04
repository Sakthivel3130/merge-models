import yaml
from mergekit.config import MergeConfiguration
from mergekit.merge import MergeOptions ,run_merge

config_yml="/home/team1/Sakthivel_f22/model_merge/merge.yml"
with open(config_yml,"r",encoding="utf-8") as fp:
    merge_config=MergeConfiguration.model_validate(yaml.safe_load(fp))

run_merge(
    merge_config,
    out_path="/home/team1/Sakthivel_f22/model_merge/merged",
    options=MergeOptions(
        copy_tokenizer=True,
        lazy_unpickle=False,
        low_cpu_memory=False
    ),
)