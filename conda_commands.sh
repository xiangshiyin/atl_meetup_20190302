conda create --name py3test
conda list --explicit
conda list --explicit > spec-file.txt
conda create --name myenv --file spec-file.txt
conda install --name myenv --file spec-file.txt
conda remove --name myenv
conda activate env-name
conda deactivate
