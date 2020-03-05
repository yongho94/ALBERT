import modeling
import run_pretraining_test

# ml1mtime vocab size : 3713
# beautytime vocab size :

fname = '/media/disk1/jyh/ALBERT/ml1mtime/config.json'
max_seq_length = 103
vocab_size = 3713

run_pretraining_test._create_config_file(fname, max_seq_length, vocab_size)