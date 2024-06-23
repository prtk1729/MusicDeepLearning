

import os, shutil
# import os from os.path


if __name__ == "__main__":
    DIR = "../MusicData/Data"
    # os.makedirs(os.path.join(DIR, "genre_reduced"))

    reduced_genre = "genre_reduced"
    for dirpath, dirnames, filename in os.walk(DIR):
        genre = dirpath.split("/")[-1]
        genres_folder = dirpath.split("/")[-2]

        # print( genre, genres_folder )

        if genres_folder == "genres_original": # hitting only once
            if genre == "genres_original":
                continue

            file = filename[0]
            path_name = os.path.join(DIR, "genre_reduced", str(genre), file )
            dest_path = os.path.join(DIR, reduced_genre, genre)

            # print(path_name, dest_path)

            # print( dest_path )
            # print( f"{dirpath}/{file}" )

            os.makedirs( dest_path ) # we are creating once for this sub-folder 
            shutil.copy( f"{dirpath}/{file}", dest_path)
