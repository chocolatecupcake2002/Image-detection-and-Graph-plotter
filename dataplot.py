<py-script>
            from PIL import Image, ImageChops
            
            img1 = document.getElementById("imagePreview")
            img2 = document.getElementById("imagePreview1")
            img1 = Image.open("1img.jpg")
            img2 = Image.open("2img.jpg")
            diff = ImageChops.difference(img1, img2)
            diff.imshow()
          </py-script>
          <script>
            const inpFile = document.getElementById("inpFile");
            const previewContainer = document.getElementById("imagePreview");
            const previewImage = previewContainer.querySelector(".image-preview__image")
            const previewDefaultText = previewContainer.querySelector(".image-preview__default-text")
          
            inpFile.addEventListener('change',function(){
              const file = this.files[0];

              if (file) {
                const reader = new FileReader();
                previewDefaultText.style.display = "none";
                previewImage.style.display = "block";

                reader.addEventListener("load",function(){
                  console.log(this);
                  previewImage.setAttribute("src",this.result);
                });
                reader.readAsDataURL(file);
              }
            });

            const inpFile1 = document.getElementById("inpFile1");
            const previewContainer1 = document.getElementById("imagePreview1");
            const previewImage1 = previewContainer1.querySelector(".image-preview__image1")
            const previewDefaultText1 = previewContainer1.querySelector(".image-preview__default-text1")
          
            inpFile1.addEventListener('change',function(){
              const file1 = this.files[0];

              if (file1) {
                const reader1 = new FileReader();
                previewDefaultText1.style.display = "none";
                previewImage1.style.display = "block";

                reader1.addEventListener("load",function(){
                  console.log(this);
                  previewImage1.setAttribute("src",this.result);
                });
                reader1.readAsDataURL(file1);
              }
            });
          