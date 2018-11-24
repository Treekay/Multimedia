import JpegCompress
import JpegDecompress

if __name__ == "__main__":
    # Compress
    compress1 = JpegCompress.Compress('./src/cartoon.jpg')
    compress2 = JpegCompress.Compress('./src/animal.jpg')
    compressedData1 = compress1.getCompressedData()
    compressedData2 = compress2.getCompressedData()
    # Decompress
    decompress1 = JpegDecompress.Decompress(compressedData1, './res/cartoon.jpg')
    decompress2 = JpegDecompress.Decompress(compressedData2, './res/animal.jpg')
    decompressImg1 = decompress1.getDecompressImg()
    decompressImg2 = decompress2.getDecompressImg()
    # Save and display image
    
    # Compare with origin Image and GIF-Compress-Algorithm