srcdir = 'images/'
dstdir = 'out/'

filenames = ls(srcdir);
for j = 1 : size(filenames)(1)
  fn = filenames(j,:);
  filepath = [srcdir,fn];
  disp 'Processing ',filepath;
  fflush(stdout); 

  img = imread(filepath);
  img_crop = imcrop(img, [197, 1, 1520, 950]);
  img_resize = imresize(img_crop, [800, 1200]);
  
  fp_out = [dstdir,fn];
  imwrite(img_resize, fp_out)
end

