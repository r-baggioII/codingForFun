package TaylorAlbums;

public class Main {
    public static void main(String[] args) {  // Correct the main method signature
        // Create some songs with float durations
        Song loveStory = new Song("Love Story", 3.55f, "Fearless");
        Song youBelongWithMe = new Song("You Belong with Me", 3.51f, "Fearless");

        // Create an album and add songs to it
        Album fearless = new Album("Fearless", 2008);
        fearless.addSong(loveStory);
        fearless.addSong(youBelongWithMe);

        // Create an album library and add the album to it
        AlbumLibrary library = new AlbumLibrary();
        library.addAlbum(fearless);

        // Display the library
        library.displayLibrary();
    }
}
