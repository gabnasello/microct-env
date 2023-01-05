# Slicer/SlicerDocker
# https://github.com/Slicer/SlicerDocker/blob/main/slicer-notebook/Dockerfile

FROM lassoan/slicer-notebook:5.0.3

# Install Slicer extensions
ADD install_SlicerExtensions.py ${HOME}/
ADD install.sh ${HOME}/
RUN bash ${HOME}/install.sh ${HOME}/Slicer/Slicer
RUN rm install_SlicerExtensions.py
RUN rm install.sh

# Install external Python packages
ADD requirements.txt .
RUN ./Slicer/bin/PythonSlicer -m pip install -r requirements.txt 

CMD ["sh", "-c", "./Slicer/bin/PythonSlicer -m jupyter notebook --port=$JUPYTERPORT --allow-root --ip=0.0.0.0 --no-browser --NotebookApp.default_url=/lab/"]