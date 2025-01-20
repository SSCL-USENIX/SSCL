
## To Run our Method 

```bash
python3 SSCL_main.py --ds=<dataset> --training_cutoff=<training_cutoff_value> --lr=<learning_rate> --wd=<weight_decay>  --label_ratio=1 --nps=<int> --bool_gpm=<bool> --b_m=<float> --bma=<float>  --analyst_labels=<int> --temp=<float>
```
- `--ds`: Specifies the name of the dataset to use.
- `--training_cutoff`: Defines the cutoff point for separating training and testing data.
- `--lr`: Sets the learning rate for the model's optimizer.
- `--wd`: Determines the weight decay for optimizer regularization.
- `--label_ratio`: Specifies the ratio of labeled data to be used during training.
- `--nps`: Number of projection samples for contrastive learning.
- `--bool_gpm`: Enables or disables the gradient projection mechanism.
- `--b_m`: Sets the batch memory ratio for training.
- `--bma`: Allocates the batch minority ratio during training.
- `--analyst_labels`: Number of labeled samples provided by analysts for semi-supervised learning.
## 1. Baseline Methods

To run the baseline methods, you can use the following command:
Below command is for HCL method and CADE
```bash
python3 SSCL_main_HCL_CADE.py --ds=<dataset> --training_cutoff=<training_cutoff_value> --lr=<learning_rate> --wd=<weight_decay> --family_info=<true_or_false> --label_ratio=1 --uncertainity=<sample_selector>
```
where:
- `--ds`: dataset name (e.g., 'api_graph', 'androzoo', 'bodmas')
- `--lr`: learning rate (e.g., 0.001)
- `--wd`: weight decay (e.g., 0.0001)
- `--training_cutoff`: training cutoff value (e.g., 12, 5)
- `--family_info`: true or false (e.g., true)
- `--uncertainity`: sample selector (e.g., 'pseudo-loss', 'cade')
- `--label_ratio`: label ratio (e.g., 1)

## 2. Continual Learning Methods:
```bash
python3 SSCL_cl.py --ds=<dataset> --training_cutoff=<training_cutoff_value> --lr=<learning_rate> --wd=<weight_decay> --cl_method=<method>
```
For MIR and CBRS

```bash
python3 SSCL_cl_implemented.py --ds=<dataset> --training_cutoff=<training_cutoff_value> --lr=<learning_rate> --wd=<weight_decay> --cl_method=<EWC_or_AGEM>
```
FOR EWC and AGEM
## Dataset:
Edit the Metadata.py file to change the dataset path.


