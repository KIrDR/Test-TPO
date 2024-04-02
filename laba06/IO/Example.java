public class Example {
    public int publicVariable;
    private String privateVariable;

    public Example() {
        publicVariable = 0;
        privateVariable = "private";
    }

    public void publicMethod() {
        System.out.println("This is a public method.");
    }

    private void privateMethod() {
        System.out.println("This is a private method.");
    }
}
