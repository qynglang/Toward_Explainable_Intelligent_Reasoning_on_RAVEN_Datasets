# Toward_Explainable_Intelligent_Reasoning_on_RAVEN_Datasets
Human relies on generalizable hierarchical perception and abstract reasoning abilities to answer complicated Raven's Progressive Matrices. In this article, We build explainable algorithms to approximate this human reasoning process. Our model implements human-like transferable object perception and domain-general rule application through Explainable-VAE (E-VAE) feature extraction model and cognitive-map reasoning back end. The E-VAE module is supervised. It extracts explainable features and represents individual objects with generalizable dimensions. We can use these dimensions to interact with objects' images and create unseen objects. The cognitive-map back-end binds the explainable features to general cognitive maps and makes inferences. It reasons at an abstract level and produces clear steps on how and why an answer is selected. The model generates answers and possible images for RAVEN problems in a human-like explainable way with high accuracy. It transfers well to unseen domains and has the potential to adapt to real-life situations. We intend to make the model more biologically possible in the future.

## Explainable-VAE
You can use the following code to train the Explainable VAE model

`$ cd E-VAE`

`$ python run_others.py -c configs/bbvae_bvae.yaml`

You can change the address of the images and labels in dataset_others.py

You can adjust the size of the training dataset by running the following line (50% of the original dataset).

`$python run_numbers.py -c configs/bbvae_bvae.yaml -p 0.5`

More information for the original beta-VAE model locate at https://github.com/AntixK/PyTorch-VAE

After training the E-VAE model, please put the checkpoint files in the CMs/log folder.

## Full Model Testing
The code for solving a single RAVEN problem is available in solve_all.py, The function takes two inputs: the RAVEN problems' images, and a “draw” index indicating whether you want to generate a figure for the problem.

You can use the following code to test the full model:

`$python run_all.py`

By default, run_all.py does not generate images.





