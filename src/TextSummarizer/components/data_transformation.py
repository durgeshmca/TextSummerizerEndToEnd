import os
from TextSummarizer.logging import logger
from TextSummarizer.config.configuration import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset,load_from_disk

class DataTransformation:
    def __init__(self,config : DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_data_to_features(self,batch_data):
        input_encodings = self.tokenizer(batch_data['dialogue'] , max_length = 1024, truncation = True )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(batch_data['summary'], max_length = 128, truncation = True)

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    def transform_data(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_data_to_features,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))
