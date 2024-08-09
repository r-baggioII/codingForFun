package TaylorAlbums;

import java.util.ArrayList;
import java.util.List;

public class AlbumLibrary{
    private List<Album> albums;

    //Constructor 
    public AlbumLibrary(){
        this.albums = new ArrayList<>();
    }

    //Add album to library
    public void addAlbum(Album album){
        this.albums.add(album); 
    }

    public void displayLibrary() {
        for (Album album : albums) {
            album.displayInfo();
            System.out.println();
        }
    }
}