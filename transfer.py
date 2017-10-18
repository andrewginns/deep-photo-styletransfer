import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--start-index", type=int, help="starting frame index")
parser.add_argument("--end-index", type=int, help="ending frame index")
parser.add_argument("--input-image-dir")
parser.add_argument("--input-seg-dir")
parser.add_argument("--style-image-path")
parser.add_argument("--style-seg-path")
parser.add_argument("--first-stage-dir")
parser.add_argument("--output-dir")
parser.add_argument("--num-iter", type=int)
parser.add_argument("--gpu", type=int, default=1)
parser.add_argument("--matt-dir")
args = parser.parse_args()

if not os.path.exists(args.first_stage_dir):
    os.makedirs(args.first_stage_dir)

if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

for i in xrange(args.start_index, args.end_index+1):
    input_image_path = "{}/{:0>5}.png".format(args.input_image_dir, i)
    input_seg_path = "{}/{:0>5}.png".format(args.input_seg_dir, i)
    part1_cmd = ' th neuralstyle_seg.lua -content_image {} -style_image {} -content_seg {} -style_seg {} -index {} -num_iterations {} -save_iter {} -print_iter 10 -gpu {} -serial {}'.format(input_image_path, args.style_image_path, input_seg_path, args.style_seg_path, i, args.num_iter, args.num_iter, args.gpu, args.first_stage_dir)

    init_image_path = "{}/out{}_t_{}.png".format(args.first_stage_dir, i, args.num_iter)
    matt_path = "{}/{:0>5}.mat".format(args.matt_dir, i)
    part2_cmd = ' th deepmatting_seg.lua -content_image {} -style_image {} -content_seg {} -style_seg {} -init_image {} -index {} -num_iterations {} -save_iter {} -print_iter 10 -gpu {} -serial {} -csr {} -f_radius 15 -f_edge 0.01'.format(input_image_path, args.style_image_path, input_seg_path, args.style_seg_path, init_image_path, i, args.num_iter,args.num_iter, args.gpu, args.output_dir, matt_path)
    print(part1_cmd)
    os.system(part1_cmd)
    print(part2_cmd)
    os.system(part2_cmd)

