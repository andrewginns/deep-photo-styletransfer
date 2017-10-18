addpath matting/
addpath gaimc/
pkg load image

input = im2double(imread('../../../gta-data/02_small_images/02781.png'));
disp('Compute Laplacian');
fflush(stdout);
[h w c] = size(input);
A = getLaplacian1(input, zeros(h, w), 1e-7, 1);
disp('Save to disk');
fflush(stdout);
n = nnz(A);
[Ai, Aj, Aval] = find(A);
    
[rp ci ai] = sparse_to_csr(A);
Ai = sort(Ai);
Aj = ci;
Aval = ai;
CSR = [Ai, Aj, Aval];
save('-mat7-binary', '../../../gta-data/02_small_laplacian/02781.mat', 'CSR');