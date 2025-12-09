docker network create tplb

docker build -t im-nginx-lb tp-A

mkdir -p shared1 shared2

cat > shared1/index.html <<'HTML'
<h1>Hello 1</h1>
HTML

cat > shared2/index.html <<'HTML'
<h1>Hello 2</h1>
HTML

docker run -d --name nginx1 --rm --network tplb -p 81:80 -v "$(pwd)/shared1":/usr/share/nginx/html:ro nginx
docker run -d --name nginx2 --rm --network tplb -p 82:80 -v "$(pwd)/shared2":/usr/share/nginx/html:ro nginx

docker run -d --name nginx-lb --network tplb -p 83:80 im-nginx-lb
