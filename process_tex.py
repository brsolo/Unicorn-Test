import sys
import os

if len(sys.argv) != 2:
    print("Usage: python file_to_compile.tex")
    sys.exit(1)

if sys.argv[1][-3:] != "tex":
    print("Usage: python file_to_compile.tex")
    sys.exit(1)

output_file = sys.argv[1]
drawings_path = "drawings"
header_file = "dev\header.txt"
footer_file = "dev\\footer.txt"

def combine_tex_files(drawings_path, output_file):
    tex_files  = [header_file]
    tex_files += [drawings_path + "/" + f for f in os.listdir(drawings_path) if f.endswith('.tex')]
    tex_files += [footer_file]

    print(tex_files)
    with open(output_file, 'w') as outfile:
        
        for tex_file in tex_files:
            with open(tex_file, 'r') as infile:
                # title = r"\subsection{" + tex_file + "}"
                if tex_file[:3] != "dev":
                    outfile.write('\\begin{figure}[h] \n\n')
                    outfile.write('\\centering \n\n')
                # outfile.write(f"{title}\n\n")
                outfile.write(infile.read())
                outfile.write('\n\n')
                if tex_file[:3] != "dev":
                    # don't include a caption if its header for footer
                    caption = r"\caption{" + tex_file[9:-4] + "}"
                    outfile.write(f'{caption} \n\n')
                    outfile.write('\\end{figure} \n\n')


    
combine_tex_files(drawings_path, output_file)
print("TeX file created:", output_file)
os.system(f"pdflatex {output_file}")
print("pdf created.")
# delete the extra files pdflatex created
os.system(f"del {output_file[:-4]}.log {output_file[:-4]}.aux {output_file[:-4]}.out")
print("extra files removed.")