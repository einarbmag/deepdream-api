FROM visionai/clouddream

RUN pip install flask

RUN cd /usr/src
RUN git clone https://github.com/einarbmag/deepdream-api.git
RUN cd deepdream-api
RUN export FLASK_APP=server.py

CMD flask run