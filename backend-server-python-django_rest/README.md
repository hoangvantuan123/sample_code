Để sử dụng Django REST framework, bạn cần cài đặt nó thông qua pip bằng cách chạy lệnh sau trong terminal:

```
pip install pipenv
pip install djangorestframework
pip install django-cors-headers
django-admin startproject project .
python manage.py startapp app
python manage.py makemigrations
python manage.py migrate
#Dat mat khau
python manage.py createsuperuser
python manage.py runserver

```

Backend là một phần quan trọng của hệ thống web, nó giúp xử lý các yêu cầu từ phía người dùng, lưu trữ và truy vấn dữ liệu từ cơ sở dữ liệu và cung cấp các dịch vụ web qua các API. Trong mô tả này, chúng ta sẽ tìm hiểu về việc sử dụng Django Rest Framework và PostgreSQL để xây dựng một backend cho một ứng dụng web.

## **Django Rest Framework**

Django là một framework phổ biến trong lập trình web, nó cung cấp một cách tiếp cận nhanh chóng và hiệu quả để xây dựng các ứng dụng web. Django Rest Framework (DRF) là một phần mở rộng của Django, nó cung cấp các công cụ và thư viện hỗ trợ để xây dựng các API RESTful cho ứng dụng web.

DRF cho phép xây dựng các API RESTful phức tạp với các tính năng như xác thực, phân quyền, serialization, thực hiện CRUD, … và nhiều tính năng khác. DRF sử dụng các Serializer để tạo ra định dạng dữ liệu phù hợp cho API. Serializer cũng hỗ trợ validation để đảm bảo tính toàn vẹn và độ chính xác của dữ liệu.

## **PostgreSQL**

PostgreSQL là một hệ quản trị cơ sở dữ liệu (DBMS) mã nguồn mở, nó được sử dụng phổ biến trong các ứng dụng web để lưu trữ và truy vấn dữ liệu. PostgreSQL có khả năng xử lý dữ liệu rất lớn và đa dạng, cung cấp các tính năng như hỗ trợ cho các kiểu dữ liệu phức tạp, đa luồng, và các tính năng quản lý dữ liệu tiên tiến.