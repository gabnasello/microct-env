# Slicer/SlicerDocker
# https://github.com/Slicer/SlicerDocker

FROM lassoan/slicer-notebook:2021-10-15-b3077c2

# Install Slicer extensions
ADD install_SlicerMorph.py ${HOME}/
ADD install.sh ${HOME}/
RUN bash ${HOME}/install.sh ${HOME}/Slicer/Slicer
RUN rm install_SlicerMorph.py
RUN rm install.sh

# Install scikit-image
RUN ./Slicer/bin/PythonSlicer -m pip install scikit-image

CMD ["sh", "-c", "./Slicer/bin/PythonSlicer -m jupyter notebook --port=$JUPYTERPORT --allow-root --ip=0.0.0.0 --no-browser --NotebookApp.default_url=/lab/"]