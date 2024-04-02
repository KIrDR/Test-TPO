private class Example {
    private int publicVariable;
    private String privateVariable;

    private Example() {
        publicVariable = 0;
        privateVariable = "private";
    }

    private void publicMethod() {
        System.out.println("This is a private method.");
    }

    private void privateMethod() {
        System.out.println("This is a private method.");
    }
}
