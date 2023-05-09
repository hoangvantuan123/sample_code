fetch('http://127.0.0.1:8000/reactapi/')
  .then(response => response.json())
  .then(data => {
    console.log(data); // In dữ liệu ra console
    // Tiếp tục xử lý dữ liệu tại đây
  })
  .catch(error => console.error(error));
