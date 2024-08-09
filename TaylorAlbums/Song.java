package TaylorAlbums;

public class Song {
    String title;
    float duration;
    String album;

    // Constructor for Song class (initializing instance variables)
    public Song(String title, float duration, String album) {
        this.title = title;
        this.duration = duration;
        this.album = album;
    }

    // Getter method for title
    public String getTitle() {
        return title;
    }

    // Getter method for duration
    public float getDuration() {
        return duration;
    }

    // Getter method for album (if needed)
    public String getAlbum() {
        return album;
    }

    // Method to display song information
    public void displayInfo() {
        System.out.println("Title: " + title + " | Duration: " + duration + " mins | Album: " + album);
    }
}
