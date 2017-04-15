FROM visionai/clouddream

RUN pip install flask

RUN git clone https://github.com/einarbmag/deepdream-api.git /usr/src/deepdream-api/
ENV FLASK_APP /usr/src/deepdream-api/server.py

CMD flask run --host=0.0.0.0