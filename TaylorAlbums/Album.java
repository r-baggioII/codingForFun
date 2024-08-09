package TaylorAlbums;
import java.util.ArrayList;
import java.util.List;

public class Album{
    String name;
    int releaseYear; 
    List<Song> songs; 

    //Constructor 
    public Album(String name, int releaseYear){
        this.name = name; 
        this.releaseYear = releaseYear; 
        this.songs = new ArrayList<Song>();
    }

    //Method to add songs to the album 
    public void addSong(Song song){
        songs.add(song); 
    }
    
    //Getters 
    public String getName(){
        return name; 
    }
    public int getReleaseYear(){
        return releaseYear; 
    }
    public List<Song> getSongs(){
        return songs; 
    }

    //Method to display info 
    public void displayInfo(){
        System.out.println("Album:" + name + "(" + releaseYear + ")");
        for(Song song: songs){
            song.displayInfo();
        }
    }
}